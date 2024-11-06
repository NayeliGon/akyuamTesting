pipeline {
    agent any

    environment {
        // Variables para los navegadores y drivers
        PATH = "/usr/local/bin:${env.PATH}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clona el repositorio
                git branch: 'main', url: 'https://github.com/NayeliGon/akyuamTesting.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Instala las dependencias especificadas en requirements.txt
                sh 'pip3 install -r requirements.txt --user'
                // Instala Geckodriver para Firefox
                sh '''
                wget https://github.com/mozilla/geckodriver/releases/latest/download/geckodriver-v0.33.0-linux64.tar.gz
                tar -xzf geckodriver-v0.33.0-linux64.tar.gz
                sudo mv geckodriver /usr/local/bin/
                rm geckodriver-v0.33.0-linux64.tar.gz
                '''
            }
        }

        stage('Prepare Test Directory') {
            steps {
                // Crea el directorio para almacenar los reportes de pruebas
                sh 'mkdir -p test-reports'
            }
        }

        stage('Run Tests') {
            steps {
                // Ejecuta las pruebas de Selenium utilizando Firefox
                sh '''
                export DISPLAY=:99
                Xvfb :99 -ac &
                python3 -m unittest discover -s tests -p "*.py" -v | tee test-reports/results.log
                '''
            }
        }

        stage('Generate Reports') {
            steps {
                // Genera el reporte de pruebas en formato JUnit
                junit 'test-reports/results.log'
            }
        }
    }

    post {
        always {
            // Limpia archivos temporales
            cleanWs()
        }
    }
}
