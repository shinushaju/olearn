from app import app, db
from app.models.enrolledCourses import Enrolled_courses
from flask_login import login_required,  current_user
from flask import request, redirect
from app.utils.student.decorators import student_role_required

@login_required
@student_role_required()
@app.route('/student/markSectionAsComplete', methods=['POST'])
def markSectionAsComplete():
    courseid=request.form['courseid']

    # Finding enrolled course
    result=Enrolled_courses.query.filter_by(student_id=current_user.id, course_id=courseid).one_or_none()
    if result is not None:
        result.completed_sections+=1
        db.session.commit()

        # Getting previous URL
        redirect_url=request.form['redirect_url']

        return redirect(redirect_url)
        
    else:
        return "Something went wrong."
