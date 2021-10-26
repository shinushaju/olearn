from flask import render_template,redirect, url_for,flash
from flask_login import login_required, current_user
from app import app,db
from app.models.courses import Course
from app.models.enrolledCourses import Enrolled_courses
from time import sleep

@app.route('/student/dashboard')
@login_required
def student_dashboard():
    available = Course.query.all() #Storing all course record in Course table to a list varaible
    enrolled = Enrolled_courses.query.filter_by(student_id = current_user.id).all()#Storing all the enrolled courses for the logged in user
    enrolledcoursesList = [] #list to store course records from course table
    
    #for finding course details with course id
    for c in enrolled:
        cid = c.course_id
        course = Course.query.filter_by(id = cid).first()
        #print(item)
        enrolledcoursesList.append(course)
    
    #for removing enrolled courses from available pane
    unenrolledCourseList = []
    for course in available:
        if course not in enrolledcoursesList:
            unenrolledCourseList.append(course)
    return render_template('student/dashboard.html', user=current_user, available = unenrolledCourseList, enrolledcoursesList = enrolledcoursesList)

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