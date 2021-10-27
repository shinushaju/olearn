from flask import render_template,redirect, url_for,flash
from flask_login import login_required, current_user
from app import app,db
from app.models.courses import Course
from app.models.enrolledCourses import Enrolled_courses
from app.models.student_review import Student_review
import math

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
    
    #for removing enrolled courses from available courses pane
    unenrolledCourseList = []
    for course in available:
        if course not in enrolledcoursesList:
            unenrolledCourseList.append(course)
    
    return render_template('student/dashboard.html', user=current_user, available = unenrolledCourseList, enrolledcoursesList = enrolled)

@app.route('/student/enroll/<cid>')
@login_required
def course_enroll(cid):
    enrolled = Enrolled_courses.query.filter_by(student_id = current_user.id, course_id = cid).all()
    #Checking whether the course is previously enrolled
    #if not, enroll the course in the enrolled_courses table
    if len(enrolled) == 0:
        db.session.add(Enrolled_courses( student_id = current_user.id, course_id = cid, progress = 1))
        db.session.commit()
    return redirect(url_for('student_dashboard'))

@app.route('/student/course/<cid>')
@login_required
def course(cid):
    course = Course.query.get(cid)
    result=Enrolled_courses.query.filter((Enrolled_courses.course_id==cid) & (Enrolled_courses.student_id==current_user.id)).one_or_none()
    enrolled=True
    if result is None:
        enrolled=False

    # Review section:
    reviews = Student_review.query.filter_by(course_id=cid).all()
    review_list=list()
    for review in reviews:
        if math.floor(review.rating)==review.rating:
            review_list.append((review, math.floor(review.rating), False))
        else:
            review_list.append((review, math.floor(review.rating), True))
    
    return render_template('student/course.html', user=current_user, course = course, enrolled=enrolled, review_list=review_list)
