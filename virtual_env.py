"""
What is a Virtual Environment?
A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.

It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.

Think of a virtual environment as a separate container for each Python project. Each container:

    Has its own Python interpreter
    Has its own set of installed packages
    Is isolated from other virtual environments
    Can have different versions of the same package

Using virtual environments is important because:

    It prevents package version conflicts between projects
    Makes projects more portable and reproducible
    Keeps your system Python installation clean
    Allows testing with different Python versions
    
"""


"""
Creating a Virtual Environment
Python has the built-in venv module for creating virtual environments.

To create a virtual environment on your computer, open the command prompt, and navigate to the folder where you want to create your project, then type this command:

Windows: python -m venv venv
Linux/Mac: python -m venv myfirstproject

- This will set up a virtual environment, and create a folder named "myfirstproject" with subfolders and files, like this:

Result
The file/folder structure will look like this:

myfirstproject
  Include
  Lib
  Scripts
  .gitignore
  pyvenv.cfg
"""

"""
Activate Virtual Environment
To use the virtual environment, you have to activate it with this command:

windows: venv\Scripts\activate
Linux/Mac:  source venv/bin/activate

after it will look this this
    PS C:\Users\user\Development\Python\Python_Fundamentals> venv\Scripts\activate
    (venv) PS C:\Users\user\Development\Python\Python_Fundamentals> 
- this means that your virtual env is activated
"""


"""
Install Packages
Once your virtual environment is activated, you can install packages in it, using pip.

We will install a package called 'cowsay':

Example
Install 'cowsay' in the virtual environment:

run in terminal(any): pip install cowsay

'cowsay' is installed only in the virtual environment:

Collecting cowsay
  Downloading cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
Downloading cowsay-6.1-py3-none-any.whl (25 kB)
Installing collected packages: cowsay
Successfully installed cowsay-6.1

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: python.exe -m pip install --upgrade pip


"""




