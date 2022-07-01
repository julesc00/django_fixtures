pipeline {
    agent any

    stages {
        stage("Run Tests") {
            steps {
                echo "Testing with UnitTest"
                sh "./manage.py test"
                echo "Testing with Pytest"
                sh "pytest"
            }
        }
        // Another stage
    }
}