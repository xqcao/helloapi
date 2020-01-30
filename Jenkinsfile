currentBuild.displayName="hello_api_job #"+currentBuild.number
pipeline{
    agent any
    environment{
        DOCKER_TAG = getDockerTagForVersion()
    }
    stages{
        stage("Build Docker Image 001"){
            steps{
                echo "========executing A build image========"
                // withCredentials([string(credentialsId: 'dockerHub', variable: 'dockerHubPwd')]) {
                //     sh "docker login -u adamcao -p ${dockerHubPwd}"
                //     sh "docker build . -t adamcao/helloapiapp:${DOCKER_TAG}"
                // }
                sh "docker build . -t adamcao/helloapiapp:${DOCKER_TAG}"

                
            }
            
        }
        stage("DockerHub Push 002"){
            steps{
                echo "====++++docker push again++++===="
                withCredentials([string(credentialsId: 'dockerHub', variable: 'dockerHubPwd')]) {
                   
                    sh "docker push adamcao/helloapiapp:${DOCKER_TAG}"
                }
            }
        }
        stage("install kubectl and get pods"){
            steps{
                // sh "curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.11.5/bin/darwin/amd64/kubectl"
                // sh "chmod +x ./kubectl"
                // sh "mv ./kubectl /usr/local/bin/kubectl"
                echo "kubectl version"
                // sh "kubectl get pods"
            }
        }
        stage("Deploy to k8s 003"){
            steps{
                echo "==== ++++ k8s deploy++++===="
                sh "cat mydev.yml"
                sh "chmod +x changeTag.sh"
                sh "./changeTag.sh ${DOCKER_TAG}"
                sh "cat my_deployment.yml"
                script{
                    try{
                        sh "kubectl apply -f my_deployment.yml"
                    }catch(error){
                        sh "kubectl create -f my_deployment.yml"
                    }
                }
            }
        }
    }
}

def getDockerTagForVersion(){
    def tag = sh script: 'git rev-parse HEAD', returnStdout: true
    return tag
}