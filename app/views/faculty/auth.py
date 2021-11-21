from os import error
from flask import render_template, redirect, session, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from app import app, db
from app.models.user import User
from app.models.faculty import Faculty
from app.utils.auth import validate_email, validate_name, validate_password

### Faculty SignUp View
@app.route('/faculty/join',methods=['GET','POST'])
def faculty_signup():
    if request.method == 'POST':
            email = request.form.get('email')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            password = request.form.get('password')
            # concatenate first name and last name
            name = first_name + ' ' + last_name

            if name and email and password:
                user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
                if user: # if a user is found, we want to redirect back to signup page so user can try again
                    flash("User already exits!", 'error')
                else:
                    if validate_name(first_name) and validate_name(last_name) and validate_email(email) and validate_password(password):
                        user = User(email=email, password=generate_password_hash(password, method='sha256'))
                        user.role = "faculty"
                        # add a new user to database
                        db.session.add(user)
                        db.session.commit()
                        # add a new faculty record
                        faculty = Faculty(name=name, faculty_id=user.id)
                        db.session.add(faculty)
                        db.session.commit()
                        flash("Sign Up Success🎉, Please Login to Continue!", "success")
                        return redirect(url_for('faculty_login'))
                    else:
                        # error messages
                        if not validate_name(first_name) or not validate_name(last_name):
                            flash("Enter a Valid Name","error")
                        if not validate_email(email):
                            flash("Enter a Valid Email","error")
                        if not validate_password(password):
                            flash("Enter a Valid Password","error")
            else:
                if not name or not email or not password:
                    flash("Fill the Mandatory Fields", "error")
    return render_template('home/faculty-signup.html')

### Faculty Login View
@app.route('/faculty/login', methods=['GET','POST'])
def faculty_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        if email and password :      
            user = User.query.filter_by(email=email).first()
            if user:
                if not check_password_hash(user.password, password):
                    flash('Invalid credentials!', "error")
                    #return redirect(url_for('faculty_login')) # if the user doesn't exist or password is wrong, reload the page
                else:
                    # if the above check passes, then we know the user has the right credentials
                    login_user(user, remember=remember)
                    flash("Login Success!", "success")
                    return redirect(url_for('faculty_dashboard'))
            else:
                flash("User doesn't exist! Please Sign Up.", "error")
        else:
                if not email or not password:
                    flash("Fill the Mandatory Fields", "error")
    return render_template('home/faculty-login.html', role="Faculty")

