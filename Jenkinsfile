pipeline {
    agent any

    stages {

        stage('Registering build artifact') {
            steps {
                script {
                    echo 'Registering the metadata'
                    echo 'Another echo to make the pipeline a bit more complex'
                    env.ARTIFACT_ID = registerBuildArtifactMetadata(
                        name: "Automation test for Register-Artifacts",
                        version: "1.0.0",
                        type: "docker",
                        url: "http://non:1111",
                        digest: "6f637064707039346163663237383938",
                        label: "Artifact"
                    )
                    echo "Captured Artifact ID: ${env.ARTIFACT_ID}"

                    // Verify artifact ID was captured successfully
                    if (!env.ARTIFACT_ID) {
                        error("Failed to capture Artifact ID from build artifact registration")
                    }
                    echo "Build artifact registration completed successfully"
                }
            }
        }

        stage('Registering deployed artifact') {
            environment {
                TARGET_ENV = 'production'
            }
            steps {
                script {
                    // Wait for build artifact registration to complete and verify artifact ID is available
                    echo "Waiting for build artifact registration to complete..."

                    if (!env.ARTIFACT_ID) {
                        error("Artifact ID is not available. Build artifact registration may have failed.")
                    }

                    echo "Artifact ID verified: ${env.ARTIFACT_ID}"
                    echo "Registering deployment to environment: ${env.TARGET_ENV}"

                    registerDeployedArtifactMetadata(
                        id: "${env.ARTIFACT_ID}",
                        targetEnvironment: "production"
                    )

                    echo "Deployment artifact registration completed successfully"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        failure {
            echo 'Build or tests failed!'
        }
    }
}
