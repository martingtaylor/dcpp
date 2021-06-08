pipeline{
    agent any
    environment {
        app_version = 'v1'
        rollback = 'false'
    }
    stages{
        stage('Test') {
            steps {
                // Run PYTEST
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
                    docker login -u martingtaylor -p Mgt2992443
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