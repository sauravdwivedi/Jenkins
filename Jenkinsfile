pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t jenkins-backend .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop jenkins-backend || true && docker rm jenkins-backend || true'
                sh 'docker run --name jenkins-backend -d -p 5000:5000 jenkins-backend'
            }
        }
    }
}