pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker build -t backend .'
                sh 'docker run -d -p 5000:5000 backend'
            }
        }
    }
}