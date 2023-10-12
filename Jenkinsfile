pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        bt 'python3 hello.py'
      }
    }
  }
}
