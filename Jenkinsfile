pipeline{
    agent any
    environment{
        DOCKER_TAG = getDockerTagForVersion()
    }
    stages{
        stage("Build DOcker Image"){
            steps{
                echo "========executing A build image========"
                sh "docker build -t adamcao/helloapiapp:${DOCKER_TAG}"
            }
            
        }
        stage("DockerHub Push"){
            steps{
                echo "====++++docker push++++===="
                sh "docker push adamcao/helloapiapp:${DOCKER_TAG}"
            }
        }
        stage("Deploy to k8s"){
            steps{
                echo "====++++k8s deploy++++===="
                sh "chmod +x changeTag.sh"
                sh "./changeTag.sh ${DOCKER_TAG}"
                script{
                    try{
                        sh "kubectl apply -f ."
                    }catch(error){
                        sh "kubectl create -f ."
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