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
    }
}