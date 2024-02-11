# Jenkins pipeline with Flask (backend) and React (frontend) apps

<img src=pic.PNG alt="Jenkins pipeline">

## Install and configure Jenkins

- https://www.jenkins.io/download/
- https://github.com/jenkinsci/docker/blob/master/README.md
- https://harshityadav95.medium.com/how-to-setup-docker-in-jenkins-on-mac-c45fe02f91c5
  
## Run Jenkins (Homebrew)
```bash
brew services start jenkins-lts
brew services restart jenkins-lts
```
- http://localhost:8080/ 

## Run Jenkins (Docker)
```bash
docker run --name jenkins -d -u 0 --privileged -p 8080:8080 -p 50000:50000 --restart=on-failure \
-v /var/run/docker.sock:/var/run/docker.sock \
-v $(which docker):/usr/bin/docker \
-v jenkins_home:/var/jenkins_home \
jenkins/jenkins:lts-jdk17
```
- http://localhost:8080/ 

## Create Jenkins pipeline

- https://www.jenkins.io/doc/pipeline/tour/hello-world/

## Clone project 

```bash
gh repo clone sauravdwivedi/Jenkins
```

## Setup git repo 
Copy project directory to a git repo and configure that repo in Jenkins pipeline. Docker should be up and running.

## Setup Docker Hub credentials

Install Docker Pipeline plugin in Jenkins, and setup docker hub credentials (Manage Jenkins -> Manage Plugins):

- https://gcore.com/learning/building-docker-images-to-docker-hub-using-jenkins-pipelines/

Modify Jenkinsfile accordingly:

```json
REGISTRY = "<Your docker hub username>/<Your repository name>"
```

## Backend and Frontend apps

If Jenkins pipeline works fine, then backend and frontend apps run on

- http://127.0.0.1:5000/api/v1/ui/
- http://127.0.0.1:3000

## Jenkins console output

<img src=log.PNG alt="Jenkins log">