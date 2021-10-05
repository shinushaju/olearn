# flask-app

> Install Virtual Environment

Python 3 comes with a virtual environment module called venv preinstalled. If you have Python 3 installed, skip this step.<br/>
If you have Python 2, follow the given instructions:

###### Install virtualenv on Windows:
`py -2 -m pip install virtualenv`<br/>
###### Install virtualenv on Linux:
`sudo apt install python-virtualenv`<br/>

> Create an Environment 'env'

Run the commands: <br/>
###### Create environment on Windows:
<b>For Python 3:</b><br/>

`py -3 -m venv env`

<b>For Python 2:</b><br/>

`py -2 -m virtualenv env`

###### Create environment on Linux:
<b>For Python 3:</b><br/>

`python3 -m venv env`

<b>For Python 2:</b><br/>

`python -m virtualenv env`

> Activate the Environment

Run the commands: <br/>

###### On Windows:

`env\Scripts\Activate.ps1`

###### On Linux:

`source env/bin/activate`

> Install Flask 

`python -m pip install flask`

> Set the FLASK_APP Environment Variable.

Run the commands: <br/>
###### On Windows:

`setx FLASK_APP=app`<br/>
`setx FLASK_APP=development`<br/>

###### On Linux:

`export FLASK_APP=app`<br/>
`export FLASK_APP=development`<br/>

> Run the Flask App

`flask run`


> Git Commands

`git init` - Initializes a git repository <br/><br/>

`git pull https://github.com/ShinuShaju/flask-app` - pulls the code from remote repository

`git add .` or `git add filename`  - adds a file/files to the git staging area <br/>
`git commit -m "commit message in double quotes"`<br/><br/>

`git branch -m main` - sets main branch as main<br/>
`git remote add origin https://github.com/ShinuShaju/flask-app`<br/>
`git remote set-url origin https://github.com/ShinuShaju/flask-app`<br/>

`git push -u origin main` - push to a remote git repository<br/>
