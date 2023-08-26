pipeline {
    agent { docker { image 'python:3.11.4-alpine3.18' } }
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Deploy') {
            steps {
                sh 'cat MatrixMultiplication.cs'
                sh 'python3'
            }
        }
    }
}