from app import app, db
from flask import render_template, request, flash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from app.models.courses import Course
from app.utils.decorators import faculty_role_required
from app.models.faculty import Faculty
from app.utils.auth import validate_email, validate_name, validate_password
### Faculty Dashboard View - only user with faculty role has access.
@app.route('/faculty/dashboard')
@login_required
@faculty_role_required()
def faculty_dashboard():
    active_courses = Course.query.filter_by(faculty_id=current_user.id, is_active=True, is_draft=False).all()
    draft_courses = Course.query.filter_by(faculty_id=current_user.id, is_draft=True, is_active=False).all()
    active_courses.reverse()
    draft_courses_count = len(draft_courses)
    return render_template('faculty/dashboard.html', user=current_user, active_courses=active_courses, draft_courses_count=draft_courses_count)

### Faculty Courses View - only user with faculty role has access.
@app.route('/faculty/courses')
@login_required
@faculty_role_required()
def faculty_courses():
    # get 'active', 'draft' and 'archived' courses from db.
    active_courses = Course.query.filter_by(faculty_id=current_user.id, is_active=True, is_draft=False).all()
    draft_courses = Course.query.filter_by(faculty_id=current_user.id, is_draft=True, is_active=False).all()
    archived_courses = Course.query.filter_by(faculty_id=current_user.id, is_draft=False, is_active=False).all()
    active_courses.reverse()
    draft_courses.reverse()
    archived_courses.reverse()
    return render_template('faculty/faculty-courses.html', user=current_user, active_courses=active_courses, draft_courses=draft_courses, archived_courses=archived_courses)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

### Faculty Profile
@app.route('/faculty_profile', methods=['GET', 'POST'])
@login_required
@faculty_role_required()
def faculty_profile():
    user = current_user
    faculty=user.faculty
    flash(faculty.name, 'debug')
    names = faculty.name.split()
    if request.method == 'POST':
        name=faculty.name
        if request.form.get('Name1') is not None and request.form.get('Name2') is not None:
            if validate_name(request.form.get('Name1')) and validate_name(request.form.get('Name2')):
                name = request.form.get('Name1')+" "+request.form.get('Name2')
            else:
                flash('Invalid name!', 'error')

        email=user.email
        if request.form.get('email') is not None:
            if validate_email(request.form.get('email')):
                email = request.form.get('email') or user.email
            else:
                flash('Invalid email!', 'error')

        gender = request.form.get('gender') or faculty.gender
        phoneNo = request.form.get('mobileNumber') or faculty.phoneNo
        address = request.form.get('address') or faculty.address
        qualification = request.form.get('qualification') or faculty.qualification
        if request.form.get('password') is not None:
            if validate_password(request.form.get('password')):
                new_password=request.form.get('password')
                user.password=generate_password_hash(new_password, method='sha256')
            else:
                flash("Password not valid!", 'error')
        user.email = email
        faculty.name = name
        faculty.gender = gender
        faculty.phoneNo = phoneNo
        faculty.address = address
        faculty.qualification = qualification
        db.session.add(user)
        db.session.commit()
        db.session.add(faculty)
        db.session.commit()
        names
        return render_template('faculty/faculty_profile.html', user=user, names=name.split())

    return render_template('faculty/faculty_profile.html',user=user, names=names)


