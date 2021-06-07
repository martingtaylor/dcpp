pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
        }
        stages{
            stage('Build Image'){
                steps{

			sh '''
			cd app1
			docker build . -t mgt/app1:latest
			'''
                }
            }
        }
}
