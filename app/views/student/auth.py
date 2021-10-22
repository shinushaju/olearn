from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
# import db model
from app.models.student import Student
from flask_login import login_user, logout_user, login_required

# sign up as a student
@app.route('/students/join',methods=['GET','POST'])
def student_signup():
    if request.method == 'POST':
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
                return redirect(url_for('student_login'))
    return render_template('home/student-signup.html')

# login as a student
@app.route('/students/login', methods=['GET','POST'])
def student_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        student = Student.query.filter_by(email=email).first()
        if not student or not check_password_hash(student.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('student_login')) # if the user doesn't exist or password is wrong, reload the page
        else:
            # if the above check passes, then we know the user has the right credentials
            login_user(student, remember=remember)
            return redirect(url_for('student_dashboard'))
    
    return render_template('home/student-login.html', role="Student")

# log out a student
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


