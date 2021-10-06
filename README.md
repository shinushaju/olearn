# flask-app

## Install Virtual Environment

Python 3 comes with a virtual environment module called venv preinstalled. If you have Python 3 installed, skip this step.<br/>
If you have Python 2, follow the given instructions:

### Installation:  
**Windows**:  
`py -2 -m pip install virtualenv`  

**Linux**:  
`sudo apt install python-virtualenv`  

### Creating a new environment named 'env'

Run the commands:  
**Windows**:  
Python 3: `py -3 -m venv env`  
Python 2: `py -2 -m virtualenv env`

**Linux**:  
Python 3: `python3 -m venv env`  
Python 2: `python -m virtualenv env`

### Activating the environment

Run the commands:  
**Windows**:  
`env\Scripts\Activate`

**Linux**:  
`source env/bin/activate`

## Installing libraries  
Libraries necessary :  
* Flask   
`python -m pip install flask`

## Running flask app

### Setting FLASK_APP Environment Variable.

Run the commands:  
**Windows**:  
`setx FLASK_APP=app`  
`setx FLASK_APP=development`  

**Linux**:  
`export FLASK_APP=app`  
`export FLASK_APP=development`  

### Run the flask app  
Command:  
`flask run`


## Git Commands

* `git init`  
        Initializes a git repository   

* `git pull https://github.com/ShinuShaju/flask-app`  
        pulls the code from remote repository  

* `git add .` or `git add filename`  
        adds a file/files to the git staging area   
* `git commit -m "commit message in double quotes"`  

* `git branch -m main`  
        sets main branch as main  
* `git remote add origin https://github.com/ShinuShaju/flask-app`  
* `git remote set-url origin https://github.com/ShinuShaju/flask-app`  

* `git push -u origin main`  
        push to a remote git repository  

