from flask import render_template
from app import app
# import db 
from app import db

# sign up as a faculty
@app.route('/faculty/join')
def faculty_signup():
    return render_template('home/faculty-signup.html')

# login as a faculty
@app.route('/faculty/login')
def faculty_login():
    return render_template('home/faculty-login.html', role="Faculty")