pipeline {
    agent any

    environment {
        ALLURE_HOME = "C:\\Tools\\allure\\allure-2.34.1"
        PATH = "${env.ALLURE_HOME}\\bin;${env.PATH}"
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Явно указываем ветку main
                git branch: 'main',
                     url: 'https://github.com/PavelVNazarov/python-qa-auto.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Установка зависимостей...'
                    bat 'python -m pip install -r requirements.txt'
                }
            }
        }
        stage('Run UI and API Tests') {
            steps {
                script {
                    echo 'Запуск тестов с Allure...'
                    bat 'pytest tests/ --alluredir=allure-results --clean-alluredir -v'
                }
            }
        }
    }

    post {
        success {
            echo 'Тесты успешно выполнены!'
        }
        failure {
            echo 'Сборка провалена: тесты упали'
        }
        always {
            allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                results: [[path: 'allure-results']]
            ])
            archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
        }
    }
}
