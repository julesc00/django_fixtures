pipeline {
    agent any

    stages {
        stage("Run Tests") {
            steps {
                echo "Testing with UnitTest"
                sh "python manage.py test"
                echo "Testing with Pytest"
                sh "pytest -vv"
            }
        }
        // Another stage
        stage("Run Bash Script") {
            steps {
                echo "[INFO] Running script."
                sh "./script.sh"
            }
        }
    }
}