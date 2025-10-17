# import subprocess

import os
import subprocess

os.system("ls")

subprocess.run(["ls"])
subprocess.run(["ls","-l"])
subprocess.run(["ls","-l","README.md"])
subprocess.run(["ls","-l","README.md"])

# Retrieving system information

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run(['ps', '-x'])


# Show all list

# def listCurrentDirectory():
#     subprocess.run(['ls', '-la'])

# Updateing system

# def updateSystem():
#     subprocess.run(['sudo', 'apt', 'update', '-y'])
#     subprocess.run(['sudo', 'apt', 'upgrade', '-y'])

# Adding user to the system
# def createUser(user):
#     user_name = input("Enter user name")
#     subprocess.run(['sudo', 'adduser', user_name])

# Introducing System Administration with Python