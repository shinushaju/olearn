from app import app, db
from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_required, current_user
from app.models.courses import Course, Lecture, Section
from app.utils.decorators import faculty_role_required

# --------------------------------------------------------------- #
### Create Course View - only user with faculty role has access.
# --------------------------------------------------------------- #
@app.route('/course/create',methods=['GET','POST'])
@login_required
@faculty_role_required()
def create_course():

    if request.method == 'POST':
        course_name = request.form.get('course_name')
        course_overview = request.form.get('course_overview')
        course_skills = request.form.get('course_skills')
        preview_link = request.form.get('preview_link')
        course_duration = request.form.get('course_duration')
        course_price = request.form.get('course_price')
        difficulty_level = request.form.get('difficulty_level')
        program = request.form.get('program')
        faculty_id = current_user.id

        if course_name and course_overview and course_skills and preview_link and course_duration and course_price  and difficulty_level and program and faculty_id:
            course = Course(course_name=course_name, course_overview=course_overview, course_skills=course_skills, preview_link=preview_link, course_duration=course_duration, course_price=course_price, difficulty_level=difficulty_level, program=program, faculty_id=faculty_id)
            # add the new course to the database
            db.session.add(course)
            db.session.commit()
            # add course_id to session
            session['course_id'] = course.id
            return redirect(url_for('add_section'))
        else:
            flash('Please enter all the mandatory fields!', 'error')

    return render_template('faculty/course/create-course.html', user=current_user)
# --------------------------------------------------------------- #


# --------------------------------------------------------------- #
### Add Section View - only user with faculty role has access.
# --------------------------------------------------------------- #
@app.route('/course/sections',methods=['GET','POST'])
@login_required
@faculty_role_required()
def add_section():

    if 'course_id' in session:
      course_id = session['course_id']

    course = Course.query.get(course_id)

    if request.method == 'POST':
        section_title = request.form.get('section_title')
        section_outcome = request.form.get('section_outcome')
        course_id = course.id
        is_active = True
        is_draft = False

        if request.form.get('action') == 'Save Section':
            if section_title and section_outcome and course_id:
                section = Section(section_title=section_title, section_outcome=section_outcome, course_id=course_id)
                db.session.add(section)
                db.session.commit()
            return redirect(url_for('add_section'))

        if request.form.get('action') == 'Add Lectures':
            section_id = request.form.get('section_id')
            session['section_id'] = section_id
            return redirect(url_for('add_lecture'))

        if request.form.get('action') == 'Save as Draft':
            is_draft = True
            is_active = False
            course.is_active = is_active
            course.is_draft = is_draft
            db.session.commit()
            session.pop('course_id', None)
            session.pop('section_id', None)
            return redirect(url_for('faculty_courses'))

        if request.form.get('action') == 'Create and Publish':
            is_draft = False
            is_active = True
            course.is_active = is_active
            course.is_draft = is_draft
            db.session.commit()
            session.pop('course_id', None)
            session.pop('section_id', None)
            return redirect(url_for('faculty_courses'))

    return render_template('faculty/course/add-section.html', user=current_user, course=course)
# --------------------------------------------------------------- #


# --------------------------------------------------------------- #
### Add Lecture View - only user with faculty role has access.
# --------------------------------------------------------------- #
@app.route('/course/section/lectures',methods=['GET','POST'])
@login_required
@faculty_role_required()
def add_lecture():

    if 'course_id' in session:
      course_id = session['course_id']
    if 'section_id' in session:
      section_id = session['section_id']

    course = Course.query.get(course_id)
    section = Section.query.get(section_id)

    if request.method == 'POST':
        if request.form.get('action') == 'Save Lecture':
            lecture_title = request.form.get('lecture_title')
            lecture_link = request.form.get('lecture_link')
            lecture_duration = request.form.get('lecture_duration')
            if lecture_title and lecture_link and lecture_duration and section_id:
                lecture = Lecture(lecture_title=lecture_title, lecture_link=lecture_link, lecture_duration=lecture_duration, section_id=section_id)
                db.session.add(lecture)
                db.session.commit()
            return redirect(url_for('add_lecture'))
   
    return render_template('faculty/course/add-lecture.html', user=current_user, course=course, section=section)
# --------------------------------------------------------------- #


# --------------------------------------------------------------- #
### Manage a Course View - only user with faculty role has access.
# --------------------------------------------------------------- #
@app.route('/course/<course_id>/manage',methods=['GET','POST'])
@login_required
@faculty_role_required()
def manage_course(course_id):
   
    '''
    if 'course_id' in session:
      session.pop('course_id', None)
    if 'section_id' in session:
      session.pop('section_id', None)
    '''
    course = Course.query.get(course_id)

    if request.method == 'POST':
        if request.form.get('action') == 'Edit Course Info':
            # add course_id to session
            session['course_id'] = course.id
            return redirect(url_for('edit_course_info'))
        
        if request.form.get('action') == 'Add New Section':
            # add course_id to session
            session['course_id'] = course.id
            return redirect(url_for('add_section'))
        
        if request.form.get('action') == 'Edit Info':
            section_id = request.form.get('section_id')
            # add course_id to session
            session['section_id'] = section_id
            return redirect(url_for('edit_section_info'))
        
        if request.form.get('action') == 'Add New Section':
            # add course_id to session
            session['course_id'] = course.id
            return redirect(url_for('add_section'))

        if request.form.get('action') == 'Publish Course':
            is_draft = False
            is_active = True
            course.is_active = is_active
            course.is_draft = is_draft
            db.session.commit()
            return redirect(url_for('faculty_courses'))

        if request.form.get('action') == 'Archive Course':
            is_draft = False
            is_active = False
            course.is_active = is_active
            course.is_draft = is_draft
            db.session.commit()
            return redirect(url_for('faculty_courses'))

    return render_template('faculty/course/manage-course.html', user=current_user, course=course)
# --------------------------------------------------------------- #


# ----------------------------------------------------------------------------- #
### Manage Lectures in a Section View - only user with faculty role has access.
# ----------------------------------------------------------------------------- #
@app.route('/course/<course_id>/section/<section_id>/lectures/manage',methods=['GET','POST'])
@login_required
@faculty_role_required()
def manage_lectures(course_id, section_id):
    session['course_id'] = course_id
    session['section_id'] = section_id
    return redirect(url_for('add_lecture'))
# ----------------------------------------------------------------------------- #


# --------------------------------------------------------------- #
### Edit Course Info View - only user with faculty role has access.
# --------------------------------------------------------------- #
@app.route('/course/info/edit',methods=['GET','POST'])
@login_required
@faculty_role_required()
def edit_course_info():
    
    if 'course_id' in session:
      course_id = session['course_id']

    course = Course.query.get(course_id)

    if request.method == 'POST':
        if request.form.get('action') == 'Update Course Info':
            course_name = request.form.get('course_name')
            course_overview = request.form.get('course_overview')
            course_skills = request.form.get('course_skills')
            preview_link = request.form.get('preview_link')
            course_duration = request.form.get('course_duration')
            course_price = request.form.get('course_price')
            difficulty_level = request.form.get('difficulty_level')
            program = request.form.get('program')

            if course_name and course_overview and course_skills and preview_link and course_duration and course_price  and difficulty_level and program:
                course.course_name = course_name
                course.course_overview = course_overview
                course.course_skills = course_skills
                course.preview_link = preview_link
                course.course_duration = course_duration
                course.course_price = course_price
                course.difficulty_level = difficulty_level
                course.program = program
                db.session.commit()
                session.pop('course_id', None)
                return redirect(url_for('manage_course', course_id = course_id))

    return render_template('faculty/course/edit-course-info.html', user=current_user, course=course)
# --------------------------------------------------------------- #


# --------------------------------------------------------------- #
### Edit Section Info View - only user with faculty role has access.
# --------------------------------------------------------------- #
@app.route('/course/<course_id>/section/<section_id>/info/edit',methods=['GET','POST'])
@login_required
@faculty_role_required()
def edit_section_info(course_id, section_id):

    course = Course.query.get(course_id)
    section = Section.query.get(section_id)

    if request.method == 'POST':
        if request.form.get('action') == 'Update Section Info':
            section_title = request.form.get('section_title')
            section_outcome = request.form.get('section_outcome')
            section.section_title = section_title
            section.section_outcome = section_outcome
            db.session.commit()
            return redirect(url_for('manage_course', course_id = course_id))
    return render_template('faculty/course/edit-section-info.html', user=current_user, course=course, section=section)
# --------------------------------------------------------------- #


# --------------------------------------------------------------- #
### Edit Lecture Info View - only user with faculty role has access.
# --------------------------------------------------------------- #
@app.route('/course/<course_id>/section/<section_id>/lecture/<lecture_id>/info/edit',methods=['GET','POST'])
@login_required
@faculty_role_required()
def edit_lecture_info(course_id, section_id, lecture_id):
    lecture = Lecture.query.get(lecture_id)
    course = Course.query.get(course_id)
    section = Section.query.get(section_id)

    if request.method == 'POST':
        if request.form.get('action') == 'Update Lecture Info':
            lecture_title = request.form.get('lecture_title')
            lecture_link = request.form.get('lecture_link')
            lecture_duration = request.form.get('lecture_duration')
            lecture.lecture_title = lecture_title
            lecture.lecture_link = lecture_link
            lecture.lecture_duration = lecture_duration
            db.session.commit()
            return redirect(url_for('add_lecture'))
    return render_template('faculty/course/edit-lecture-info.html', user=current_user, course=course, section=section, lecture=lecture)
# --------------------------------------------------------------- #


# --------------------------------------------------------------- #
### Delete a Section View - only user with faculty role has access.
# --------------------------------------------------------------- #
@app.route('/course/<course_id>/section/<section_id>/delete',methods=['GET','POST'])
@login_required
@faculty_role_required()
def delete_section(course_id, section_id):
    section = Section.query.get(section_id)
    if section:
        db.session.delete(section)
        db.session.commit()
    return redirect(url_for('manage_course', course_id=course_id))
# --------------------------------------------------------------- #


# --------------------------------------------------------------- #
### Delete a Lecture View - only user with faculty role has access.
# --------------------------------------------------------------- #
@app.route('/course/section/lecture/<lecture_id>/delete',methods=['GET','POST'])
@login_required
@faculty_role_required()
def delete_lecture(lecture_id):
    lecture = Lecture.query.get(lecture_id)
    if lecture:
        db.session.delete(lecture)
        db.session.commit()
    return redirect(url_for('add_lecture'))
# --------------------------------------------------------------- #
