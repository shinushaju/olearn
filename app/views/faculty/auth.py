from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
# import db model
from app.models.faculty import Faculty
from flask_login import login_user, logout_user, login_required

# sign up as a faculty
@app.route('/faculty/join',methods=['GET','POST'])
def faculty_signup():
    if request.method == 'POST':
            email = request.form.get('email')
            name = request.form.get('name')
            password = request.form.get('password')
            user = Faculty.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
            
            if user: # if a user is found, we want to redirect back to signup page so user can try again
                return redirect(url_for('faculty_signup'))
            else:
                faculty = Faculty(email=email, name=name, password=generate_password_hash(password, method='sha256'))
                # add the new faculty to the database
                db.session.add(faculty)
                db.session.commit()
                return redirect(url_for('faculty_login'))
    return render_template('home/faculty-signup.html')

# login as a faculty
@app.route('/faculty/login', methods=['GET','POST'])
def faculty_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        faculty = Faculty.query.filter_by(email=email).first()
        if not faculty or not check_password_hash(faculty.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('faculty_login')) # if the user doesn't exist or password is wrong, reload the page
        else:
            # if the above check passes, then we know the user has the right credentials
            login_user(faculty, remember=remember)
            return redirect(url_for('faculty_dashboard'))
    
    return render_template('home/faculty-login.html', role="Faculty")

# log out a faculty
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


