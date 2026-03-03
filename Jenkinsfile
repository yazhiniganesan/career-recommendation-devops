pipeline {
    agent any

    environment {
        IMAGE_NAME = "career-app"
        CONTAINER_NAME = "career-container"
    }

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/yazhiniganesan/career-recommendation-devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests..."
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }
    }

    post {
        success {
            mail to: 'developer@gmail.com',
                 subject: "Build Success: ${env.JOB_NAME}",
                 body: "Deployment successful!"
        }

        failure {
            mail to: 'developer@gmail.com',
                 subject: "Build Failed: ${env.JOB_NAME}",
                 body: "Check Jenkins immediately!"
        }
    }
}
