pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t backend .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop backend || true && docker rm backend || true'
                sh 'docker run --name backend -d -p 5000:5000 backend'
            }
        }
    }
}