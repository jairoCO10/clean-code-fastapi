pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/jairoCO10/clean-code-fastapi.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install --upgrade pip'
                sh 'pip install -r libraries/requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest'
            }
        }
    }

    post {
        always {
            junit 'tests/reports/*.xml'  // Si estás generando reportes JUnit
            archiveArtifacts 'tests/reports/*.xml'
            cleanWs()
        }
    }
}
