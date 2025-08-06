pipeline {
    agent any

    environment {
        EC2_USER = 'ec2-user'
        //EC2_IP = '44.201.168.167'
        EC2_IP = '3.93.20.227'
        //#SSH_KEY_ID = '76500835-54f1-424d-b6aa-78ecb2bbf8fe' // ID of the SSH key added in Jenkins credentials
        SSH_KEY_ID = '3094bad0-b614-4dfc-aaa8-932a174dc41c'
    }
    triggers {
        githubPush()
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/ryadav0198/jenkinscode.git'
            }
        }
        stage('Build Docker Image'){
            steps {
                sh 'sudo docker build -t python-app .'
            }
        }

        stage('Deploy and copy to EC2') {
            steps {
                sshagent (credentials: ["${SSH_KEY_ID}"]) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} 'mkdir -p ~/python-app/'
                    scp -o StrictHostKeyChecking=no -r * ${EC2_USER}@${EC2_IP}:~/python-app/
                    """
                }
            }
        }

        stage('Run Docker and Python Script') {
            steps {
                sshagent (credentials: ["${SSH_KEY_ID}"]) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} 'cd /home/ec2-user/python-app &&
                        sudo docker stop python-app || true &&
                        sudo docker rm python-app || true &&
                        sudo docker build -t python-app . &&
                        sudo docker run -d --name python-app python-app'
                    """
                }
            }
        }
    }
}