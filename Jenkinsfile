pipeline{
    agent any
    environment{
        DOCKER_TAG = getDockerTagForVersion()
    }
    stages{
        stage("Build DOcker Image"){
            steps{
                echo "========executing A========"
                sh "docker build -t adamcao/helloapiapp:${DOCKER_TAG}"
            }
            
        }
        stage("DockerHub Push"){
            steps{
                // withCredentials([string(credentialsId:'docker-hub',variable:'dockerHunPwd')]){
                //     sh "docker login -u adamcao -p ${dockerHunPwd}"
                //     sh "docker push adamcao/helloapiapp:${DOCKER_TAG}"
                // }
                sh "docker push adamcao/helloapiapp:${DOCKER_TAG}"

            }
        }
        stage("Deploy to k8s"){
            stages{
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
    def tag = sh script: 'get rev-parse HEAD', returnStdout: true
    return tag
}