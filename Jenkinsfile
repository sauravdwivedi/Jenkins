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
                sh 'docker run -it $(docker build -q .)'
            }
        }
    }
}