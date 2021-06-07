pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
        }
        stages{
            stage('Build Images'){
                steps{
			sh '''
			cd app1
			docker build . -t mgt/app1:latest
			'''

                        sh '''
                        cd app2
                        docker build . -t mgt/app2:latest
                        '''
                        
			sh '''
                        cd app3
                        docker build . -t mgt/app3:latest
                        '''

                        sh '''
                        cd app4
                        docker build . -t mgt/app4:latest
                        '''

                }
            }
        }
}

