pipeline {
    agent docket {
        image 'python:3.7.17'
    }

    environment {
        DOCKER_BUILDKIT = '1'
        TOKEN = credentials('file-env')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                url: 'https://github.com/jairoCO10/clean-code-fastapi.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install --upgrade pip'
                sh 'pip install -r libraries/requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                withCredentials([String, 'file', 'FILE']) {

                }
                sh '. venv/bin/activate && pytest --junitxml=tests/reports/results.xml'
            }
        }
    }

    post {
        always {
            junit 'tests/reports/results.xml'
            archiveArtifacts artifacts: 'tests/reports/results.xml', allowEmptyArchive: true
            cleanWs()
        }
    }
}
