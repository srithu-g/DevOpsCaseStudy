pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image"
                bat "docker build -t srithu/casestudy:latest ."
            }
        }

        stage('Docker Login') {
            steps {
                bat "docker login -u srithu -p Docker@123"
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker image to Docker Hub"
                bat "docker push srithu/casestudy:latest"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes"
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}