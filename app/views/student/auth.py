from flask import render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
# import db model
from app.models.student import Student

# sign up as a student
@app.route('/students/join',methods=['POST'])
def student_signup():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user = Student.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
    
    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('student_signup'))
    else:
        student = Student(email=email, name=name, password=generate_password_hash(password, method='sha256'))
        # add the new user to the database
        db.session.add(student)
        db.session.commit()
    return render_template('home/student-signup.html')

# login as a student
@app.route('/students/login')
def student_login():
    return render_template('home/student-login.html', role="Student")
