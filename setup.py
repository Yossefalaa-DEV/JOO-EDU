import os
import subprocess
import sys

def run_command(command):
    process = subprocess.Popen(command, shell=True)
    process.wait()
    return process.returncode

def main():
    # Create Django project
    run_command('django-admin startproject jooedu .')
    
    # Create apps
    run_command('python manage.py startapp accounts')
    run_command('python manage.py startapp courses')
    run_command('python manage.py startapp videos')
    
    # Create frontend directory
    os.makedirs('frontend', exist_ok=True)
    
    print("Project structure created successfully!")

if __name__ == '__main__':
    main() 