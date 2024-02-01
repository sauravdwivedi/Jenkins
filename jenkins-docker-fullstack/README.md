# Jenkins pipeline with flask backend and React frontend apps

<img src=pic.PNG alt="Jenkins pipeline">

## Install and configure Jenkins

- https://www.jenkins.io/download/
- https://github.com/jenkinsci/docker/blob/master/README.md
- https://harshityadav95.medium.com/how-to-setup-docker-in-jenkins-on-mac-c45fe02f91c5

## Run Jenkins (Homebrew)
```bash
brew services start jenkins
brew services restart jenkins
```
- http://localhost:8080/ 

## Run Jenkins (Docker)
```bash
docker run --name jenkins -d -p 8080:8080 -p 50000:50000 --restart=on-failure jenkins/jenkins:lts-jdk17 
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
registry = "<Your docker hub username>/<Your repository name>"
```

## Backend app

If Jenkins pipeline works fine, then backend app runs on

- http://127.0.0.1:5000/api/v1/ui/

## Jenkins console output

<img src=log.PNG alt="Jenkins log">