#!/usr/bin/env python3

# This is for linux system with VS Code, Virtual Env and Git installed.

import os
import time
import sys

def create_necessary_files(projectname):
    os.mknod('requirements.txt')
    os.mknod('info.txt')
    os.system('virtualenv ' + projectname + 'Env')
    os.system('git init')
    #os.system('source ' + projectname + 'Env/bin/activate') Still in need of fixing

def __main__():

    projectname = sys.argv[1]
    
    time.sleep(1.5)
    print('Setting up ' + projectname + ' project')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(2)

    #Actual code
    desiredlocation = 'bluej/Documents/Projects'
    if os.getcwd() != desiredlocation:
        while os.getcwd() != '/home':
            os.chdir('..')
            
        # Checking if they have a Projects file in their Documents folder
        try:
            os.mkdir(desiredlocation)
        except FileExistsError as e:
            print('You already have a /Projects Directory in your Documents folder. Great!')
            os.chdir(desiredlocation)

        try:
            os.chdir(desiredlocation)
        except FileNotFoundError as e:
            print('')

    #Making and entering the project directory
    os.mkdir(projectname)
    os.chdir(projectname)

    #Creating the necessary files
    create_necessary_files(projectname)

    os.system('code .')

    print('Process Finished')
    


if __name__ == '__main__':
    __main__()
