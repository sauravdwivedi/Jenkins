pipeline {
    environment {
        registry = "sauravdwivedi/jenkins-example-app"
        registryCredential = 'dockerhub_id'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Build') {
            script {
                dockerImage = docker.build registry + ":$BUILD_NUMBER"
            }
            // steps {
            //     sh 'docker build -t jenkins-backend .'
            // }
        }
        stage('Deploy') {
            script {
                docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                }
            }
            steps {
                sh 'docker stop dockerImage || true && docker rm dockerImage || true'
                sh 'docker run --name jenkins-backend -d -p 5000:5000 dockerImage'
            }
        }
    }
}