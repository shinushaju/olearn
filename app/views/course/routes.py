from flask import render_template, request, url_for, redirect
from app import app, db
from app.models.discussions import Query
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
