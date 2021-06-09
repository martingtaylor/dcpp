pipeline{
    agent any
    environment {
        app_version = 'v1'
        rollback = 'false'
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
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
    }
}