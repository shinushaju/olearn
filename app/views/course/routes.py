from flask import render_template, request, url_for, redirect
from app import app, db
from app.models.discussions import Query, Reply
from app.models.faculty import Faculty
from flask_login import login_required, current_user

@app.route('/course')
def course_page():
    return render_template('course/course-page.html')


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

#course/<course-id>/discussion


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
