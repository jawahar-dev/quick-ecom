pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'quickcomImage'
        CONTAINER_NAME = 'quickcomContainer'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build DOCKER_IMAGE
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    docker.run('-p 5000:5000 --name ' + CONTAINER_NAME + ' ' + DOCKER_IMAGE)
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker ps'
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    sh 'docker stop ' + CONTAINER_NAME
                    sh 'docker rm ' + CONTAINER_NAME
                }
            }
        }
    }

    post {
        always {
            script {
                sh 'docker rmi -f $(docker images -q)'
            }
        }
    }
}
