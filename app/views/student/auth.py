from flask import render_template
from app import app
# import db 
from app import db

# sign up as a student
@app.route('/students/join')
def student_signup():
    return render_template('home/student-signup.html')

# login as a student
@app.route('/students/login')
def student_login():
    return render_template('home/student-login.html', role="Student")
