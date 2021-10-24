from flask import render_template
from app import app

@app.route('/course')
def course_page():
    return render_template('course/course-page.html')
