pipeline {
 agent any
  stages {
    stage('run test') {
      steps {
        sh 'python3 -m pytest /tests/api/test_request.py -v -m api'
      }
    }
  }
}