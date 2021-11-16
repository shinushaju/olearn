from app import app
from flask import render_template, session
from flask_login import login_required, current_user
from app.models.courses import Course
from app.utils.decorators import faculty_role_required

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
