pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
        }
        stages{
            stage('Test'){
                steps{
                    
                }
            }
        }
        stages{
            stage('Build Images'){
                steps{
			        sh '''
			            docker-compose build
			        '''
                }
            }
            stage('Upload to Docker Hub') {
                steps{
                    sh '''
                        docker login -u martingtaylor -p Mgt2992443
                    '''

                    sh '''
                        docker-compose push

                        #docker tag app1 martingtaylor/app1
                        #docker push martingtaylor/app1
                        #docker tag app2 martingtaylor/app2
                        #docker push martingtaylor/app2
                        #docker tag app3 martingtaylor/app3
                        #docker push martingtaylor/app3
                        #docker tag app4 martingtaylor/app4
                        #docker push martingtaylor/app4                    
                    '''

                    sh '''
                        docker logout
                    '''
                }
            }
        }
}

