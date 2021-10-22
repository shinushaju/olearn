from flask import render_template

from app import app, db
from app.models.courses import Course

@app.route('/students/create-dummy-courses')
def createDummyCourses():
    db.session.add(Course(course_name='Course 1', course_description='Description 1', course_duration=200, course_price=10000))
    db.session.add(Course(course_name='Course 2', course_description='Description 2', course_duration=100, course_price=5000))
    db.session.add(Course(course_name='Course 3', course_description='Description 3', course_duration=50, course_price=1000))
    db.session.commit()

    return "<html><body><h1>Dummy courses created</h2></body></html>"

    