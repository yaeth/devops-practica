pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        sh 'docker build -t demo .'
      }
    }

    stage('Push') {
      steps {
        sh 'docker push demo'
      }
    }

    stage('Deploy') {
      steps {
        sh 'kubectl apply -f k8s/'
      }
    }
  }
}
