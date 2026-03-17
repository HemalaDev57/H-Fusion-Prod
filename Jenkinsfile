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
                        name: "h-e2e-dm",
                        version: "1.0.1",
                        type: "docker",
                        url: "docker.io/hemaladev57/h-e2e-dm:1.0.1",
                        digest: "1123f6370647070393461636632373839386",
                        label: "prod"
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
                    url: "docker.io/hemaladev57/h-e2e-dm:1.0.1",
                    targetEnvironment: "PREPROD",
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
                        name: "h-e2e-dm-1",
                        version: "1.0.2",
                        type: "docker",
                        url: "docker.io/hemaladev57/h-e2e-dm-1:1.0.2",
                        digest: "11223b63706470703934616366323738393856",
                        label: "prod"
                    )
                    echo "Artifact output is: ${artifactOutput1}"
                    env.ARTIFACT_ID = artifactOutput1
                    def artifactOutput2 = registerBuildArtifactMetadata(
                        name: "h-e2e-dm-2",
                        version: "1.0.0",
                        type: "docker",
                        url: "docker.io/hemaladev57/h-e2e-dm-2:1.0.0",
                        digest: "11223ba3706470703934616366323738393856",
                        label: "prod"
                    )
                    echo "Artifact output is: ${artifactOutput2}"
                    env.ARTIFACT_ID_1 = artifactOutput2
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
                    url: "docker.io/hemaladev57/h-e2e-dm-1:1.0.2",
                    targetEnvironment: "Production",
                    labels: "prod"
                )    
                echo "Artifact ID : ${env.ARTIFACT_ID_1}"
                registerDeployedArtifactMetadata(
                    id: "${env.ARTIFACT_ID_1}",
                    url: "docker.io/hemaladev57/h-e2e-dm-2:1.0.0",
                    targetEnvironment: "Production",
                    labels: "prod"
                )    
                echo 'Deploying...'
                sleep 2
            }
        }
    }
}
