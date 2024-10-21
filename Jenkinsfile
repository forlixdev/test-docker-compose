pipeline {
    agent {label "dind"}
    stages {
        stage('Build') {
          steps {
            container('docker-dind') {
              sh 'docker compose run test'
                }
            }
        }
    }
}