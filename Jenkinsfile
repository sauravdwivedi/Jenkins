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
                sh 'docker run -d -p 5000:5000 backend'
            }
        }
    }
}