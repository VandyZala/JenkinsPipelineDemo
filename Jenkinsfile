pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('hello') {
      steps {
        bat 'python hello.py'
      }
    }
    stage('Selenium') {
      steps {
        bat 'python Jankins_automation.py'
      }
    }
  }
}
