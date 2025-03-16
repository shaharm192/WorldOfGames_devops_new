pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/shaharm192/WorldOfGames_devops_new.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t world-of-games-rest-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    docker stop rest_app || true
                    docker rm rest_app || true
                    docker run -d -p 5001:5001 --name rest_app world-of-games-rest-app
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker exec rest_app python docker_backend_testing.py'
            }
        }
    }
}