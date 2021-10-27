from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from app import app, db
from app.models.courses import Course
from app.models.student_review import Student_review
import math

@login_required
@app.route('/student/student_review/<cid>',methods=['GET','POST'])
def student_review(cid):
    "This function takes reviews and publish it"
    if request.method == "POST":  
        subject = request.form["subject"]  
        rating = request.form["rating"]  
        r1 = Student_review(student_id=current_user.id,course_id=cid, subject=subject,rating=rating)
    
        db.session.add(r1)
        db.session.commit()

        return redirect(url_for('show_review'))
    return render_template('student/student_review.html',user=current_user)

@app.route('/student/show_review')
def show_review():
    reviews = Student_review.query.all()
    return render_template('student/show_review.html',reviews=reviews,user=current_user)   

@app.route('/student/delete_review')
def delete_review():
    Student_review.query.delete()
    return "<html><body><h1>All reviews are deleted Successfully</h1></body></html>"
    