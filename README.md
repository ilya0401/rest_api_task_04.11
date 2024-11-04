
<!-- описание репозитория -->
# The Project checks Userinterface of web-application

### Requirements for working with the project:
1. Git (https://git-scm.com/download/win)
2. Python 3.9 (https://www.python.org/downloads/)
3. PyCharm or any other IDE with support for Python development (https://www.jetbrains.com/pycharm/download/)


### Steps to set up a project locally:

1. Prepare a local directory with no Cyrillic symbols in path `mkdir -p user_interface`, `cd user_interface`
2. Clone repository using Git: `git clone https://github.com/ilya0401/rest_api_task_04.11.git`
3. Create virtual environment in the Project `python -m venv .venv` 
4. Activate virtual environment `.venv\Scripts\activate`
5. Add Python 3.9 Interpreter to the environment **see hint #2**
6. Install requirements `pip install -r requirements.txt`
7. Run any test, make sure the test is completed without errors
8. If tests fails - try **hint 3**




### HINTS:

#### 1. Steps for adding Interpreter to the Project virtual Environment:
  1. Open PyCharm and go to project settings: File > Settings (или Ctrl + Alt + S).
  2. Choose the Project section: <Project name> > Project Interpreter.
  3. Click on the gear icon and select Add....
  4. Select in opened window "Existing environment" and specify the path to your environment (usually: your_project_name\\venv\\Scripts\\python.exe for Windows).
  5. Add the interpreter and apply the changes.

#### 2. Make sure the virtual environment is created and activated:
    
  File -> Settings -> Project(Name og project) -> Python Interpreter:\
  Python 3.9 is installed to venv to the root of the Project

#### 3. If tests fail check the following:
  * Versions of requirements are compatible: pay attention to selenium version and webdriver-manager \
    (on the moment of writing this Readme.md the following versions are working correctly:\
    selenium == 4.11.2 webdriver-manager==4.0.1)
  * Clear cache: __pycash folder in Project folder
  * Delete the broken driver file (new ones will be created):\
    C:\Users\<smth_like_user>\.wdm\gw0\drivers\chromedriver\win64\128.0.6613.137\chromedriver-win32
  * If project doesn't run after these steps contact to **Vlad Ulanow**

### Project support:
* gitignore file:
    Keep the file up to date to avoid cluttering the remote repo\
    Make sure not to send cache and logs to the remote repo\

* Before pushing commits:
    Alt + 0 (Open Commit tab on left top corner)\
    add files to .gitignore in a timely manner
    Inspect what are you pushing\
    Mark the files which are needed to be pushed (leave all local stuff locally, for instance: cache, log)\


