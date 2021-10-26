from flask import render_template, redirect, url_for, request, flash
from app import app, db
from flask_login import login_required, current_user
from app.models.faculty import Faculty
from app.models.courses import Course

# create a course
@app.route('/course/create',methods=['GET','POST'])
@login_required
def create_course():
    courses = Course.query.all()
    if request.method == 'POST':
        course_name = request.form.get('course_name')
        course_overview = request.form.get('course_overview')
        course_skills = request.form.get('course_skills')
        course_duration = request.form.get('course_duration')
        course_price = request.form.get('course_price')
        program = request.form.get('program')
        faculty_id = current_user.id

        if course_name and course_overview and course_skills and course_duration and course_price and program and faculty_id:
            course = Course(course_name=course_name, course_overview=course_overview, course_skills=course_skills, course_duration=course_duration, course_price=course_price, program=program, faculty_id=faculty_id)
            # add the new course to the database
            db.session.add(course)
            db.session.commit()
            return redirect(url_for('create_course'))

    return render_template('faculty/create-course.html', user=current_user, courses=courses)
