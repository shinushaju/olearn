from flask import render_template, session
from app import app
from flask_login import login_required, current_user
from app.models.courses import Course, Section, Lecture
from app.utils.decorators import faculty_role_required

@app.route('/course/<course_id>/preview')
def course_preview(course_id):
    #print(session)
    course = Course.query.get(course_id)
    if 'current_section_id' and 'current_lecture_id' in session:
        section_id = session['current_section_id']
        lecture_id = session['current_lecture_id']
        section = Section.query.get(section_id)
        lecture = Lecture.query.get(lecture_id)
    else:
        section = course.sections[0]
        lecture = section.lectures[0]
    return render_template('course/preview/course-preview.html', user=current_user, course=course, section_id=section.id, lecture_id=lecture.id)


@app.route('/course/<course_id>/section/<section_id>/lecture/<lecture_id>')
@login_required
@faculty_role_required()
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
    return render_template('course/course-page.html', user=current_user, course=course, section=section, lecture=lecture, current_section_id=current_section_id, current_lecture_id=current_lecture_id)

