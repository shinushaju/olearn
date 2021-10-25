from flask import render_template, request
from app import app, db

@app.route('/student/student_details', methods=['GET','POST'])
def student_details():
    if request.method == 'POST':
            roll_no = request.form.get('roll_no')
            mobile_num = request.form.get('mobile_num')
            date_of_birth = request.form.get('date_of_birth')
            student_bio = request.form.get('student_bio')

            student_detail=student_details(roll_no=roll_no, mobile_num=mobile_num,date_of_birth=date_of_birth,student_bio=student_bio)
            db.session.add(student_detail)
            db.session.commit()
            return 'Successful'
    return render_template('/student/student-details.html')