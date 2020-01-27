test jenkins pipelines

docker run --name onejenkins -p 8080:8080 -p 50000:50000 -v \$(which docker):/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins

docker run -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock --name jenkins getintodevops/jenkins-withdocker:lts

docker run -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock --name twojenkins bbjenkins:latest

docker run --name onejenkins -p 8080:8080 -p 50000:50000 -v \$(which docker):/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock bbjenkins

docker run --name zzjenkins -p 8080:8080 -p 50000:50000 -v \$(which docker):/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock bbjenkins:1.0
