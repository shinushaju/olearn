from datetime import datetime

from flask import render_template, request
from flask_login import login_required, current_user

from app import app, db
from app.models.student_details import Student_details

@login_required
@app.route('/student/student_details/<id>', methods=['GET','POST'])
def student_details(id):
    if request.method == 'POST':
        roll_no = request.form.get('roll_no')
        mobile_num = request.form.get('mobile_num')

        # Creating a date object from date string in form
        date_of_birth=datetime.strptime(request.form.get('date_of_birth'), "%Y-%m-%d").date()

        student_bio = request.form.get('student_bio')
        student_detail=Student_details(student_id=id, roll_no=roll_no, mobile_num=mobile_num,date_of_birth=date_of_birth,student_bio=student_bio)
        db.session.add(student_detail)
        db.session.commit()
        return 'Successful'
    return render_template('/student/student_details.html', user=current_user)