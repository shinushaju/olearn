from datetime import datetime

from flask import render_template, request,flash, redirect, url_for
from flask_login import login_required, current_user

from app import app, db
from app.models.student_details import Student_details
from app.utils.student.validate_phone import validate_phone
from app.utils.student.decorators import student_role_required


@login_required
@student_role_required()
@app.route('/student/student_details', methods=['GET','POST'])
def student_details():
        if request.method == 'POST':
                roll_no = request.form.get('roll_no')
                mobile_num = request.form.get('mobile_num')
                # Creating a date object from date string in form
                date_of_birth=datetime.strptime(request.form.get('date_of_birth'), "%Y-%m-%d").date()
                student_bio = request.form.get('student_bio')
 
                res = Student_details.query.filter_by(student_id=current_user.id).one_or_none()

                if validate_phone(mobile_num)==True:
                        if res==None:
                                student_detail=Student_details(student_id=current_user.id, roll_no=roll_no, mobile_num=mobile_num,date_of_birth=date_of_birth,student_bio=student_bio)
                                db.session.add(student_detail)
                                db.session.commit()
                                flash("Details added successfully", 'success')
                                return redirect(url_for('student_details'))

                        else:
                                res.roll_no = roll_no
                                res.mobile_num = mobile_num
                                res.date_of_birth = date_of_birth
                                res.student_bio = student_bio
                                db.session.commit()
                                flash("Details updated successfully", 'success')
                                return redirect(url_for('student_details'))
                else:
                        flash('Enter a valid Mobile Number', 'error')
                        
        res = Student_details.query.filter_by(student_id=current_user.id).one_or_none()
        
        if res==None:
                #Entering for first time- Return empty string to form
                form1 = {"roll_no" : "" , "mob" : "" , "dob" : "" , "bio" : ""}

        else:
                #Profile details already present- Return edata from DB to form
                form1 = {"roll_no" : res.roll_no , "mob" : res.mobile_num , "dob" : res.date_of_birth , "bio" : res.student_bio, }
        return render_template('/student/student_details.html', user=current_user, form1=form1)