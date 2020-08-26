pipeline {
 agent any
  stages {
    stage('run test') {
      steps {
        sh 'python3 -m pytest tests/api/test_request.py -v -m api --alluredir allure-results'
      }
    }
    stage('run test') {
      steps {
        sh 'allure jdk: "", report: "/var/jenkins_home/workspace/otus_project_pipeline/allure-results", results: [[path: "allure-results"]]'
      }
    }
  }
}