pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo/ml-jenkins-pipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ml-model-app .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub', url: '']) {
                    sh 'docker tag ml-model-app your-dockerhub/ml-model-app:latest'
                    
                }
            }
        }

        stage('Deploy Model') {
            steps {
                sh 'docker run -d -p 5000:5000 your-dockerhub/ml-model-app:latest'
            }
        }
    }
}
