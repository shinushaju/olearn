from flask import render_template, redirect, url_for, request, flash, session
from app import app, db
from flask_login import login_required, current_user
from app.models.faculty import Faculty
from app.models.courses import Course, Lecture, Section

# create a course
@app.route('/course/create',methods=['GET','POST'])
@login_required
def create_course():
    if request.method == 'POST':
        course_name = request.form.get('course_name')
        course_overview = request.form.get('course_overview')
        course_skills = request.form.get('course_skills')
        course_duration = request.form.get('course_duration')
        course_price = request.form.get('course_price')
        difficulty_level = request.form.get('difficulty_level')
        program = request.form.get('program')
        faculty_id = current_user.id

        if course_name and course_overview and course_skills and course_duration and course_price  and difficulty_level and program and faculty_id:
            course = Course(course_name=course_name, course_overview=course_overview, course_skills=course_skills, course_duration=course_duration, course_price=course_price, difficulty_level=difficulty_level, program=program, faculty_id=faculty_id)
            # add the new course to the database
            db.session.add(course)
            db.session.commit()
            # add course_id to session
            session['course_id'] = course.id

            return redirect(url_for('add_section'))
        else:
            flash('Please enter all the mandatory fields!', 'error')
    return render_template('faculty/create-course.html', user=current_user)


# add section to a new course
@app.route('/course/section/add',methods=['GET','POST'])
@login_required
def add_section():

    if 'course_id' in session:
      course_id = session['course_id']
      
    course = Course.query.get(course_id)
    sections = Section.query.all()
    if request.method == 'POST':
        section_title = request.form.getlist('section_title[]')
        section_outcome = request.form.getlist('section_outcome[]')
        course_id = course.id
        for i in range(len(section_title)):
            if section_title[i] and section_outcome[i] and course_id:
                section = Section(section_title=section_title[i], section_outcome=section_outcome[i], course_id=course_id)
                db.session.add(section)
                db.session.commit()
        return redirect(url_for('add_lecture'))
    return render_template('faculty/add-section.html', user=current_user, course=course, sections=sections)

# add lecture to a new course
@app.route('/course/section/lecture/add',methods=['GET','POST'])
@login_required
def add_lecture():
    
    if 'course_id' in session:
      course_id = session['course_id']

    course = Course.query.get(course_id)
    sections = Section.query.filter_by(course_id=course_id).all()
    
    if request.method == 'POST':

        section_ids = request.form.getlist('section_id[]')
        lecture_titles = request.form.getlist('lecture_title[]')
        lecture_links = request.form.getlist('lecture_link[]')
        lecture_durations = request.form.getlist('lecture_duration[]')

        is_active = True
        is_draft = False
        if request.form.get('action') == 'Save as Draft':
            is_draft = True
            is_active = False
        
        course.is_active = is_active
        course.is_draft = is_draft
        db.session.commit()

        for i in range(len(section_ids)):
            if lecture_titles[i] and lecture_links[i] and lecture_durations[i] and course_id:
                lecture = Lecture(lecture_title=lecture_titles[i], lecture_link=lecture_links[i], lecture_duration=lecture_durations[i], section_id=section_ids[i])
                db.session.add(lecture)
                db.session.commit()
        
        session.pop('course_id', None)
        return redirect(url_for('faculty_courses'))
        
    return render_template('faculty/add-lecture.html', user=current_user, course=course, sections=sections)