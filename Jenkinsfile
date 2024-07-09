pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = '1'
        PATH = "/usr/local/bin:/usr/bin:/bin:/path/to/python3" // Añade la ruta correcta a python3
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jairoCO10/clean-code-fastapi.git'
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
