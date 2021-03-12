# This code is to Automate SSH to my Raspberry Pi and update it.
# Luma Naser
# CNA 335 Winter 3/11/2021

import paramiko
# create client ssh object so we can use it to connect to the server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # THE MISSING KEY WILL BE ADDED

ssh.connect('192.168.1.7', username='pi', password='123456')

stdin, stdout, stderr = ssh.exec_command('''sudo apt-get update ''')  
stdin.flush()
data = stdout.read().splitlines()
for line in data:
    print(line)

ssh.close()
