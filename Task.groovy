pipeline {
    agent any
    
    stages {
        stage('Launch EC2 instance') {
            steps {
                script {
                    def awsRegion = 'us-east-1'
                    def amiId = 'ami-06e46074ae430fba6' 
                    def instanceType = "${INSTANCE_TYPE}"
                    def subnetId = 'subnet-09f78d1a52da215a7'
                    def securityGroupId = 'sg-0491b07b158e71c41'
                    def keyPairName = 'key-pair-a1'

                    def instanceId = sh(script: """
                        aws ec2 run-instances \
                            --region ${awsRegion} \
                            --image-id ${amiId} \
                            --instance-type ${instanceType} \
                            --subnet-id ${subnetId} \
                            --security-group-ids ${securityGroupId} \
                            --key-name ${keyPairName} \
                            --query 'Instances[0].InstanceId' \
                            --output text
                    """, returnStdout: true).trim()

                    echo "Launched EC2 instance with ID: ${instanceId}"
                }
            }
        }
    }
}
