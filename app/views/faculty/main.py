from flask import render_template
from app import app
from sqlalchemy import and_, or_, not_
from flask_login import login_required, current_user
from app.models.courses import Course, Lecture, Section

@app.route('/faculty/dashboard')
@login_required
def faculty_dashboard():
    return render_template('faculty/dashboard.html', user=current_user)


@app.route('/faculty/courses')
@login_required
def faculty_courses():
    # get 'active' and 'draft' courses from db.
    active_courses = Course.query.filter_by(faculty_id=current_user.id, is_active=True).all()
    draft_courses = Course.query.filter_by(faculty_id=current_user.id, is_active=False).all()
    return render_template('faculty/faculty-courses.html', user=current_user, active_courses=active_courses, draft_courses=draft_courses)
