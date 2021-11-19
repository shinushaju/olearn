from flask import render_template, session
from flask.helpers import url_for
from werkzeug.utils import redirect
from app import app
import math
from flask_login import login_required, current_user
from app.models.courses import Course, Section, Lecture
from app.models.student_review import Student_review
from app.models.enrolledCourses import Enrolled_courses

@app.route('/course/<course_id>/preview')
def course_preview(course_id):
    print(session)
    course = Course.query.get(course_id)

    if 'current_section_id' and 'current_lecture_id' in session:
        course_sections = []
        course_lectures = []

        for section in course.sections:
            course_sections.append(section.id)
            for lecture in section.lectures:
                course_lectures.append(lecture.id)

        section_id = session['current_section_id']
        lecture_id = session['current_lecture_id']
   
        if int(section_id) in course_sections:
            section = Section.query.get(section_id)
        else:
            section = course.sections[0]
        if int(lecture_id) in course_lectures:
            lecture = Lecture.query.get(lecture_id)
        else:
            lecture = section.lectures[0]
    else:
        section = course.sections[0]
        lecture = section.lectures[0]
    
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
    if current_user.is_authenticated and current_user.is_student():
        result=Enrolled_courses.query.filter_by(student_id=current_user.id, course_id=course_id).one_or_none()
        if result is None:
            can_write_review=False

    if current_user.is_authenticated:
        if current_user.id == course.faculty.id:
            course_owner = True
        else:
            course_owner = False

        # Enroll/Drop section:
        # If student is already enrolled, present DROP facility
        # Else present ENROLL facility
        result=Enrolled_courses.query.filter((Enrolled_courses.course_id==course_id) & (Enrolled_courses.student_id==current_user.id)).one_or_none()
        enrolled=False
        completed=0
        if result is not None:
            enrolled=True
            completed=result.completed_sections
    else:
        course_owner = False
        enrolled = False
        completed = 0

    return render_template('course/preview/course-preview.html', user=current_user, course=course, section_id=section.id, lecture_id=lecture.id, enrolled=enrolled, course_owner=course_owner, completed=completed, review_list=review_list, can_write_review=can_write_review)


@app.route('/course/<course_id>/section/<section_id>/lecture/<lecture_id>')
@login_required
def course_page(course_id, section_id, lecture_id):

    session['course_id'] = course_id
    session['current_section_id'] = section_id
    session['current_lecture_id'] = lecture_id
    #print(session)
    course = Course.query.get(course_id)
    section = Section.query.get(section_id)
    lecture = Lecture.query.get(lecture_id)
    current_section_id = section.id
    current_lecture_id = lecture.id

    if current_user.is_authenticated:

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

        if current_user.is_student() and not enrolled:
            return redirect(url_for('student_dashboard'))

        if current_user.is_faculty() and not current_user.id == course.faculty.id:
            return redirect(url_for('faculty_dashboard'))

    return render_template('course/course-page.html', user=current_user, course=course, section=section, lecture=lecture, current_section_id=current_section_id, current_lecture_id=current_lecture_id, review_list=review_list, enrolled=enrolled, can_write_review=can_write_review, completed_sections=completed)

