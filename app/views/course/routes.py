from flask import render_template, session, request, url_for, redirect
from app import app, db
from flask_login import login_required, current_user
from app.models.courses import Course, Section, Lecture
from app.models.discussions import Query, Reply
from app.models.faculty import Faculty
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

@app.route('/discussions', methods=['GET', 'POST'])
@login_required
def course_discussions():
    queries = Query.query.all()
    if request.method == 'POST':
        query_text = request.form['query_text']
        student_name = "Harry Potter"
        course_name = "Data science"
        query = Query(query_text=query_text, student_name=student_name, course_name=course_name)
        db.session.add(query)
        db.session.commit()
        return redirect(url_for('course_discussions'))
    return render_template('course/discussions.html', user=current_user, queries=queries)

@app.route('/discussions', methods=['GET', 'POST'])
@login_required
def course_reply():
    replies = Reply.query.all()
    if request.method == 'POST':
        reply_text = request.form['reply_text']
        faculty_id = 123
        reply = Reply(reply_text=reply_text,
                      faculty_id=Faculty.id)
        db.session.add(reply)
        db.session.commit()
        return redirect(url_for('course_reply'))
    return render_template('course/discussions.html', user=current_user, replies=replies)

@app.route('/query', methods=['GET', 'POST'])
@login_required
def post_query():
    form=dict()
    form['query_title']=""
    form['query_text']=""
    
    # POST section
    if request.method=='POST':
        form['query_title']=request.form.get('query_title').strip()
        form['query_text']=request.form.get('query_text').strip()
        new_query=Query(course_id=session['course_id'], query_title=form['query_title'], query_text=form['query_text'], user_id=current_user.id)
        db.session.add(new_query)
        db.session.commit()
        return redirect(url_for('course', course_id=session['course_id'], lecture_id=session['lecture_id']))

    return render_template('course/post-query.html', form=form, user=current_user)

