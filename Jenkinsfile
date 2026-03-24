pipeline {
    agent any

    stages {
        stage('Build') {
            stages {
                stage('Compile') {
                    steps {
                        echo 'Compiling...'
                        sleep 3
                    }
                }
                stage('Package') {
                    steps {
                        echo 'Packaging...'
                        sleep 3
                    }
                }
            }
        }

        stage('Registering build artifact') {
            steps {
                script {
                    echo 'Registering the metadata'
                    echo 'Another echo to make the pipeline a bit more complex'
                    def artifactOutput = registerBuildArtifactMetadata(
                        name: "h-e2e-prod-v5",
                        version: "1.0.1",
                        type: "docker",
                        url: "docker.io/hemaladev57/h-e2e-prod-v5:1.0.1",
                        digest: "11223344556677870393461636632373839379",
                        label: "preprod"
                    )
                    echo "Artifact output is: ${artifactOutput}"
                    env.ARTIFACT_ID = artifactOutput
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                sleep 2
            }
        }

        stage('Deploy') {
            steps {
                echo "Artifact ID : ${env.ARTIFACT_ID}"
                registerDeployedArtifactMetadata(
                    id: "${env.ARTIFACT_ID}",
                    url: "docker.io/hemaladev57/h-e2e-prod-v5:1.0.1",
                    targetEnvironment: "preprod",
                    labels: "prod"
                )    
                echo 'Deploying...'
                sleep 2
            }
        }
        stage('Registering build artifact - 1') {
            steps {
                script {
                    echo 'Registering the metadata'
                    echo 'Another echo to make the pipeline a bit more complex'
                    def artifactOutput1 = registerBuildArtifactMetadata(
                        name: "h-e2e-prod-v5-1",
                        version: "1.0.1",
                        type: "docker",
                        url: "docker.io/hemaladev57/h-e2e-prod-v5-1:1.0.1",
                        digest: "11223355446677870393461636632373832388",
                        label: "prod"
                    )
                    echo "Artifact output is: ${artifactOutput1}"
                    env.ARTIFACT_ID = artifactOutput1
                }
            }
        }

        stage('Test - 1') {
            steps {
                echo 'Running Unit Tests...'
                sleep 2
            }
        }

        stage('Deploy-1') {
            steps {
                echo "Artifact ID : ${env.ARTIFACT_ID}"
                registerDeployedArtifactMetadata(
                    id: "${env.ARTIFACT_ID}",
                    url: "docker.io/hemaladev57/h-e2e-prod-v5-1:1.0.1",
                    targetEnvironment: "production-invalid",
                    labels: "prod"
                )    
                echo 'Deploying...'
                sleep 2
            }
        }
    }
}
