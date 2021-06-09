pipeline{
    agent any
    environment {
        app_version = 'v1'
        rollback = 'false'
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
    }
    stages{
        stage('Test') {
            steps {
                // Run PYTEST
                sh '''
                    echo TESTING
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
                '''

                sh '''
                    docker-compose push                   
                '''

                sh '''
                    docker logout
                '''
            }
        }
    }
}