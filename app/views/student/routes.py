from flask import render_template,redirect, url_for,flash
from flask_login import login_required, current_user
from app import app,db
from app.models.courses import Course
from app.models.enrolledCourses import Enrolled_courses

@app.route('/student/dashboard')
@login_required
def student_dashboard():
    # available = Course.query.all()
    available=Course.query.filter()
    enrolled = Enrolled_courses.query.filter_by(student_id = current_user.id).all()
    enrolledcoursesList = []
    for c in enrolled:
        cid = c.course_id
        item = Course.query.filter_by(id = cid).first()
        print(item)
        enrolledcoursesList.append(item)
    #print(enrolledcoursesList[0])
    return render_template('student/dashboard.html', user=current_user, available = available, enrolledcoursesList = enrolledcoursesList)

@app.route('/student/enroll/<sid>/<cid>')
@login_required
def course_enroll(sid, cid):
    enrolled = Enrolled_courses.query.filter_by(student_id = current_user.id, course_id = cid).all()
    if len(enrolled) == 0:
        db.session.add(Enrolled_courses(student_id = sid, course_id = cid, progress = 0))
        db.session.commit()
    else:
        flash("Already enrolled course.")
    return redirect(url_for('student_dashboard'))