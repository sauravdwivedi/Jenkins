pipeline {
    environment {
        registry = "sauravdwivedi/jenkins-example-app"
        registryCredential = 'dockerhub_id'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
                // sh 'docker build -t jenkins-backend .'
            }
        }
        stage('Deploy') {
            steps {
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
                sh 'docker stop $registry:$BUILD_NUMBER || true && docker rm $registry:$BUILD_NUMBER || true'
                sh 'docker run --name jenkins-backend -d -p 5000:5000 $registry:$BUILD_NUMBER'
            }
        }
    }
}