from flask import render_template

from app import app, db
from app.models.courses import Course

@app.route('/students/create-dummy-courses')
def createDummyCourses():
    "This function deletes all records in course table and inserts 4 course records."
    db.create_all()
    Course.query.delete()
    db.session.add(Course(course_name='Cloud DevOps Engineer', course_description='Dummy description - change this in views/student/createDummyCourses.py if you wish', course_duration=200, course_price=10000))
    db.session.add(Course(course_name='Intro to Python Programming', course_description='Dummy description - change this in views/student/createDummyCourses.py if you wish', course_duration=100, course_price=5000))
    db.session.add(Course(course_name='Data Science and Statistics', course_description='Dummy description - change this in views/student/createDummyCourses.py if you wish', course_duration=50, course_price=1000))
    db.session.add(Course(course_name='Intro to Machine Learning', course_description='Dummy description - change this in views/student/createDummyCourses.py if you wish', course_duration=72, course_price=3000))
    db.session.commit()

    return "<html><body><h2>4 Dummy courses created</h2></body></html>"

    