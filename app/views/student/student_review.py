from operator import le
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_required, current_user

from app import app, db
from app.models.courses import Course, Section, Lecture
from app.models.student_review import Student_review
from app.utils.student.decorators import student_role_required
import math

@app.route('/student/student_review/<course_id>/',methods=['GET','POST'])
@login_required
@student_role_required()
def student_review(course_id):

    form=dict()
    form['review_text']=""
    form['rating']=float(0)

    res = Student_review.query.filter_by(student_id=current_user.id, course_id=course_id).one_or_none()
    # Abhiram: pre-populate form fields if review already exists
    if res is not None:
        form['review_text']=res.review_text
        form['rating']=res.rating
    if request.method == "POST":  
        review_text = request.form.get("review_text")
        rating = request.form.get("rating") 
        if res==None:
            if review_text and rating:
                r1 = Student_review(student_id=current_user.id,course_id=course_id, review_text=review_text,rating=float(rating))
                db.session.add(r1)
                db.session.commit()
                flash("Review posted successfully", 'success')
                
                if 'current_section_id' and 'current_lecture_id' in session:
                    section_id = session['current_section_id']
                    lecture_id = session['current_lecture_id']
                    return redirect(url_for('course_page', course_id=course_id, section_id=section_id, lecture_id=lecture_id))
                else:
                    return redirect(url_for('course_preview', course_id=course_id))
        else:
            res.review_text=review_text
            res.rating=rating
            db.session.commit()
            flash("Review updated successfully", 'success')

            if 'current_section_id' and 'current_lecture_id' in session:
                section_id = session['current_section_id']
                lecture_id = session['current_lecture_id']
                return redirect(url_for('course_page', course_id=course_id, section_id=section_id, lecture_id=lecture_id))
            else:
                return redirect(url_for('course_preview', course_id=course_id))
        
    return render_template('student/student_review.html',user=current_user, form=form)

@app.route('/student/delete_review')
@login_required
@student_role_required()
def delete_review():
    Student_review.query.delete()
    return "<html><body><h1>All reviews are deleted Successfully</h1></body></html>"