pipeline {
    agent {
        label 'docker-slave'
    }
    stages {
        stage('GIT-CODE') {
            steps {
                git branch: 'master', url: 'https://github.com/nk-naveen/Jenkins-assignment'
            }
        }
        stage('CONTINOUS-INTEGRATION') {
            steps {
                sh 'python3 $WORKSPACE/Cal/testcalculator.py'
            }
        }
        stage('CONTINOUS-DEPLOYMENT/DELIVERY') {
            environment {
                STACK_NAME = 'cont-del'
                S3_BUCKET = 'aws-sam-cli-managed-default-samclisourcebucket-mj6zdx1naar'
            }
            steps {
                withAWS(credentials: 'aws creds', region: 'us-east-1') {
                    sh 'sam deploy --stack-name $STACK_NAME -t template.yaml --s3-bucket $S3_BUCKET --capabilities CAPABILITY_IAM'
                }
            }
        }
    }
}
