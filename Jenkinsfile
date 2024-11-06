pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/NayeliGon/akyuamTesting.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt --user'
            }
        }
        stage('Download and Setup Geckodriver') {
            steps {
                // Usa el enlace correcto para la versión más reciente de geckodriver
                sh 'wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz'
                sh 'tar -xvzf geckodriver-v0.35.0-linux64.tar.gz'
                sh 'chmod +x geckodriver'
                sh 'mv geckodriver /usr/local/bin'
            }
        }
        stage('Prepare Test Directory') {
            steps {
                sh 'mkdir -p test-reports'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover -s tests -p "*.py" -v | tee test-reports/results.log'
            }
        }
        stage('Generate Reports') {
            steps {
                junit 'test-reports/*.xml'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
