from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models.quizzes import Quiz, Question
from flask_login import login_required, current_user

# create a quiz
@app.route('/faculty/course/quiz/create',methods=['GET','POST'])
@login_required
def create_quiz():
    quizzes = Quiz.query.all()
    if request.method == 'POST':
        quiz_title = request.form.get('quiz_title')
        course_name = "Data Science"
        pass_percentage = request.form.get('pass_percentage')
        is_active = True
        if quiz_title and course_name and pass_percentage:
            quiz = Quiz(quiz_title=quiz_title, course_name=course_name ,pass_percentage=pass_percentage,is_active = is_active)
            # add the new quiz to the database
            db.session.add(quiz)
            db.session.commit()
            return redirect(url_for('add_question'))

    return render_template('faculty/quiz/create-quiz.html', user=current_user, quizzes=quizzes)

# create a question
@app.route('/faculty/course/quiz/add/question',methods=['GET','POST'])
@login_required
def add_question():
    questions = Question.query.all()
    quizzes = Quiz.query.all()
    if request.method == 'POST':
        question_no = request.form.get('question_no')
        question_text = request.form.get('question_text')
        option_one = request.form.get('option_one')
        option_two = request.form.get('option_two')
        option_three = request.form.get('option_three')
        option_four = request.form.get('option_four')
        answer = request.form.get('answer')
        quiz_id = request.form.get('quiz_id')
        if question_no and question_text and option_one and option_two and option_three and option_four and answer and quiz_id:
            question = Question(question_no=question_no, question_text=question_text, option_one=option_one, option_two=option_two, option_three=option_three, option_four=option_four, answer=answer, quiz_id=quiz_id)
            # add the new quiz to the database
            db.session.add(question)
            db.session.commit()
            return redirect(url_for('add_question'))

    return render_template('faculty/quiz/add-question.html', user=current_user, questions=questions, quizzes=quizzes)

# view all quizzes
@app.route('/faculty/quizzes')
@login_required
def faculty_quizzes():
    quizzes = Quiz.query.all()
    return render_template('faculty/quiz/quizzes.html', user=current_user, quizzes=quizzes)


# view all quizzes
@app.route('/faculty/quizzes/<quiz_id>')
@login_required
def view_quiz(quiz_id):
    quiz = Quiz.query.get(quiz_id)
    return render_template('faculty/quiz/view-quiz.html', user=current_user, quiz=quiz)

