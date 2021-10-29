from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app import app, db
from app.models.courses import Course
from app.models.student_review import Student_review
import math

@login_required
@app.route('/student/student_review/<cid>/<lid>',methods=['GET','POST'])
def student_review(cid,lid):
    "This function takes reviews and publish it"
    if request.method == "POST":  
        review_text = request.form.get("review_text")
        rating = request.form.get("rating") 
        res = Student_review.query.filter_by(student_id=current_user.id).one_or_none()
        if res==None:
            r1 = Student_review(student_id=current_user.id,course_id=cid,lecture_id=lid, review_text=review_text,rating=float(rating))
            db.session.add(r1)
            db.session.commit()
            flash("Details added successfully", 'success')
            return redirect(url_for('course', course_id=cid,lecture_id=lid))
        else:
            res.review_text=review_text
            res.rating=rating
            db.session.commit()
            flash("Details updated successfully", 'success')
            return redirect(url_for('course', course_id=cid,lecture_id=lid))
        

    return render_template('student/student_review.html',user=current_user)

@app.route('/student/delete_review')
def delete_review():
    Student_review.query.delete()
    return "<html><body><h1>All reviews are deleted Successfully</h1></body></html>"
    