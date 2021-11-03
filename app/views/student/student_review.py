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

    form=dict()
    form['review_text']=""
    form['rating']=float(0)

    res = Student_review.query.filter_by(student_id=current_user.id, course_id=cid).one_or_none()
    # Abhiram: pre-populate form fields if review already exists
    if res is not None:
        form['review_text']=res.review_text
        form['rating']=res.rating

    if request.method == "POST":  
        review_text = request.form.get("review_text")
        rating = request.form.get("rating") 
        if res==None:
            r1 = Student_review(student_id=current_user.id,course_id=cid, review_text=review_text,rating=float(rating))
            db.session.add(r1)
            db.session.commit()
            flash("Review posted successfully", 'success')
            return redirect(url_for('course', course_id=cid,lecture_id=lid))
        else:
            res.review_text=review_text
            res.rating=rating
            db.session.commit()
            flash("Review updated successfully", 'success')
            return redirect(url_for('course', course_id=cid,lecture_id=lid))
        

    return render_template('student/student_review.html',user=current_user, form=form)

@app.route('/student/delete_review')
def delete_review():
    Student_review.query.delete()
    return "<html><body><h1>All reviews are deleted Successfully</h1></body></html>"