pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Unit Testing') {
            steps {
                sh 'python3 -m pytest -v'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=DVP-WEEK12-CICD-SONARQUBE-DOCKER \
                    -Dsonar.sources=. \
                    -Dsonar.exclusions=test_app.py
                    '''
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t dvp-week12-app .'
            }
        }
    }
}
