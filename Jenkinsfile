pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building the Project...'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying the Project...'
      }
    }
    stage('Test') {
      steps {
        bat 'Testing the Project...'
      }
    }
  }
}
