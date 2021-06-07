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
			            docker build . -t app1:latest
			        '''

                    sh '''
                        cd app2
                        docker build . -t app2:latest
                    '''
                        
			        sh '''
                        cd app3
                        docker build . -t app3:latest
                    '''

                    sh '''
                        cd app4
                        docker build . -t app4:latest
                    '''
                }
            }
            stage('Upload to Docker Hub') {
                steps{
                    sh '''
                        docker login -u martingtaylor -p Mgt2992443
                    '''

                    sh '''
                        docker tag app1 martingtaylor/app1
                        docker push martingtaylor/app1
                        docker tag app2 martingtaylor/app2
                        docker push martingtaylor/app2
                        docker tag app3 martingtaylor/app3
                        docker push martingtaylor/app3
                        docker tag app4 martingtaylor/app4
                        docker push martingtaylor/app4                    
                    '''

                    sh '''
                        docker logout
                    '''
                }
            }
            stage('Starting Application') {
                steps{
                    sh '''
                        docker run -d --name app1 app1
                        docker run -d --name app2 app2
                        docker run -d --name app3 app3
                        docker run -d --name app3 app4
                    '''
                }
            }
        }
}

