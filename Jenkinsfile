pipeline {
 agent any
  stages {
    stage('run test') {
      steps {
        sh 'python3 -m pytest tests/api/test_request.py -v -m api --alluredir allure-results'
      }
    }
    stage('allure report') {
      steps {
        sh 'allure includeProperties: false, jdk: "", results: [[path: "/var/jenkins_home/workspace/otus_project_pipeline/allure-results"]]'
      }
    }
  }
}