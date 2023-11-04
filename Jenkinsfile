pipeline {
    environment {
        registry = "sauravdwivedi/jenkins-example-app"
        registryCredential = 'dockerhub_id'
        dockerImage = ''
        containerLog = "***************************************************container-logs***************************************************"
    }
    agent any
    stages {
        stage('Build, tag and push container') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy container') {
            steps {
                sh 'docker stop jenkins-backend || true && docker rm jenkins-backend || true'
                sh 'docker run --name jenkins-backend -d -p 5000:5000 $registry:$BUILD_NUMBER'
            }
        }
        stage('Check container logs') {
            steps {
                sh(returnStdout: false, returnStatus: true, script: 'echo $containerLog')
                sh 'docker logs jenkins-backend'
            }
        }
    }
}