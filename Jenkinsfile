pipeline {
    agent any

    environment {
        IMAGE_NAME = "career-app"
        CONTAINER_NAME = "career-container"
    }

    stages {

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
}
