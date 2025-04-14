pipeline {
    agent any

    environment {
        IMAGE_NAME = 'world-of-games-rest-app'
        CONTAINER_NAME = 'rest_app'
        DOCKERHUB_USER = 'shaharm192'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/shaharm192/WorldOfGames_devops_new.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                echo "Dummy Score: 555" > dummy_Scores.txt
                docker run -d -p 8777:5001 --name $CONTAINER_NAME -v $(pwd)/dummy_Scores.txt:/Scores.txt $IMAGE_NAME
                '''
            }
        }

        stage('Test') {
            steps {
                sh 'sleep 5' 
                sh 'python3 e2e.py || exit 1'
            }
        }

        stage('Finalize') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME
                docker rm $CONTAINER_NAME
                docker tag $IMAGE_NAME $DOCKERHUB_USER/$IMAGE_NAME:latest
                docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASSWORD
                docker push $DOCKERHUB_USER/$IMAGE_NAME:latest
                '''
            }
        }
    }
}
