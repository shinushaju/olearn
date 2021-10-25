from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models.quizzes import Quiz, Question
from flask_login import login_required, current_user

# create a quiz
@app.route('/course/quiz/create',methods=['GET','POST'])
@login_required
def create_quiz():
    quizzes = Quiz.query.all()
    if request.method == 'POST':
        quiz_title = request.form.get('quiz_title')
        course_name = request.form.get('course_name')
        if quiz_title and course_name:
            quiz = Quiz(quiz_title=quiz_title, course_name=course_name)
            # add the new quiz to the database
            db.session.add(quiz)
            db.session.commit()
            return redirect(url_for('create_quiz'))

    return render_template('faculty/create-quiz.html', user=current_user, quizzes=quizzes)
