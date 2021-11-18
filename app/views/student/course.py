
from flask import render_template, session, redirect, url_for, flash
from flask_login import login_required, current_user
import math

from flask_sqlalchemy.model import camel_to_snake_case

from app import app, db
from app.models.courses import Course, Lecture
from app.models.student_review import Student_review
from app.models.enrolledCourses import Enrolled_courses
from app.utils.student.decorators import student_role_required

@login_required
@student_role_required()
@app.route("/student/course/<course_id>/lecture/<lecture_id>")
def course(course_id, lecture_id):
    # Setting current course in session
    session['course_id']=course_id

    # Getting course from database
    course=Course.query.get(course_id)

    # Getting lecture from database
    lecture=Lecture.query.get(lecture_id)

    # Review section:
    reviews = Student_review.query.filter_by(course_id=course_id).all()
    review_list=list()
    for review in reviews:
        if math.floor(review.rating)==review.rating:
            review_list.append((review, math.floor(review.rating), False))
        else:
            review_list.append((review, math.floor(review.rating), True))
    
    # Only allow students [TODO: who have completed] who have enrolled
    # to this course to write a review.
    can_write_review=True
    ## result=Enrolled_courses.query.filter(Enrolled_courses.student_id==current_user.id) & Enrolled_courses.course_id==course_id)
    result=Enrolled_courses.query.filter_by(student_id=current_user.id, course_id=course_id).one_or_none()
    if result is None:
        can_write_review=False

    # Enroll/Drop section:
    # If student is already enrolled, present DROP facility
    # Else present ENROLL facility
    result=Enrolled_courses.query.filter((Enrolled_courses.course_id==course_id) & (Enrolled_courses.student_id==current_user.id)).one_or_none()
    enrolled=False
    completed=0
    if result is not None:
        enrolled=True
        completed=result.completed_sections

    return render_template('course/student/course-page.html', user=current_user, course=course, lecture=lecture, review_list=review_list, enrolled=enrolled, can_write_review=can_write_review, completed_sections=completed)

@login_required
@student_role_required()
@app.route("/student/drop-course/<course_id>")
def drop_course(course_id):
    Enrolled_courses.query.filter((Enrolled_courses.student_id == current_user.id) & (Enrolled_courses.course_id == course_id)).delete()
    db.session.commit()
    flash('Course unenrolled successfully.', 'success')
    return redirect(url_for('student_dashboard'))