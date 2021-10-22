from flask import render_template

from app import app, db
from app.models.enrolledCourses import Enrolled_courses

@app.route('/students/enrolled-courses')
def enrolledCourses():
    db.session.add(Enrolled_courses(student_id=1, course_id=1, progress=0))
    db.session.add(Enrolled_courses(student_id=2, course_id=2, progress=25))
    db.session.add(Enrolled_courses(student_id=3, course_id=3, progress=100))
    db.session.commit()
    courses=Enrolled_courses.query.all()
    return render_template('student/enrolled-courses.html', courses=courses)