pipeline{
    agent any
    environment {
        app_version = 'v1'
        rollback = 'false'
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
        DATABASE_URI    = credentials('DATABASE_URI')
    }
    stages{
        stage('Requirements') {
            steps {
                sh '''
                    sudo apt-get update
                    sudo apt-get install python3-pip -y
                    pip3 install -r requirements.txt
                '''
            }
        }
        stage('Testing') {
            steps {
                // Run PYTEST
                sh '''
                    python3 -m pytest -s --cov --cov-report term-missing --cov-config=.coveragerc --cov-report html
                '''
            }
        }
        stage('Build Images') {
            steps {
	            sh '''
                    docker system prune --force --all
		            docker-compose build
		        '''
            }
        }
        stage('Upload to Docker Hub') {
            steps {
                sh '''
                    docker login --username $DOCKER_USERNAME --password $DOCKER_PASSWORD
                    docker-compose push                   
                    docker logout
                '''
            }
        }
        stage('Configuration') {
            steps {
                sh '''
                    cd ansible
                    ansible-playbook -i inventory.yaml playbook.yaml
                '''
            }
        }
        stage('Deployment') {
            steps {
                sh '''
                    # copy over compose yaml to manager node
                    scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@dcppmanager:/home/jenkins/docker-compose.yaml

                    # docker stack deploy
                    ssh -i ~/.ssh/ansible_id_rsa jenkins@dcppmanager << EOF
                        export DATABASE_URI=$DATABASE_URI
                        docker stack deploy --compose-file docker-compose.yaml animal_noises
EOF
                '''
            }
        }
    }
}