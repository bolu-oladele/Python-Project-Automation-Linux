# Python-Project-Automation-Linux

This is a python script that will automated the initial stages of making a project in python. It will find your Projects Directory and then create in it a file for your project with requirements.txt, info.txt, a virtual machine set up inside of it and an empty git repository made within the project file.

This configuration is for linux do it's file system. A version for windows should soon be added to the repo.

# System Requirements - A Linux System

To run this code effectively you will have have the following installed:

- Python
- Virtual Env
- Git

NOTE: Earlier versions may require you to create your own file in your /Documents directory called Projects. Please check commit messages or comments in the script to check if you require this. \*\*\* This feature has since been included in the script.

# Configuration

Once configured please change the value in the 'desiredlocation' variale denoted by '<User name>' to the name of your user on your machine.

-- To Call From Any Directory:

As you should see from looking at the top of the file there is a short shabang script thi partially enable the running of the script from any location.

You will need to run this code in your terminal 'chmod +x makeproject.py' while in the same directory as the file.
Then you will need to move the script file from which ever directory it is currently in to the usr/bin file (you will have to past the /home directory for this).

You can do this in the terminal by running the command 'mv makeproject.py ../../../../usr/bin'. The seemingly excessive '../' are to ensure you actually make it to the outer most directory which will give you access to the /usr directory.

After this has been done you will be able to run the code using 'makeproject.py projectname'.
