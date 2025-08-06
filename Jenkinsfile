pipeline {
    agent any

    environment {
        EC2_USER = 'ec2-user'
        EC2_IP = '44.201.168.167'
        SSH_KEY_ID = '76500835-54f1-424d-b6aa-78ecb2bbf8fe' // ID of the SSH key added in Jenkins credentials
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/ryadav0198/jenkinscode.git'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent (credentials: ["${SSH_KEY_ID}"]) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} 'mkdir -p ~/python-app/app'
                    scp -o StrictHostKeyChecking=no app/main.py ${EC2_USER}@${EC2_IP}:~/python-app/app/
                    """
                }
            }
        }

        stage('Run Python Script') {
            steps {
                sshagent (credentials: ["${SSH_KEY_ID}"]) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} 'python3 ~/python-app/app/main.py'
                    """
                }
            }
        }
    }
}