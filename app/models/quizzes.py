from app import db
import datetime
#from app.models.courses import Course

# quiz model
class Quiz(db.Model):

    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True)
    quiz_title = db.Column(db.String(120), nullable=False)
    course_name = db.Column(db.String(120), nullable=False)
    pass_percentage = db.Column(db.Integer(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    is_active = db.Column(db.Boolean, default=False, nullable=False)

    questions = db.relationship("Question", back_populates="quiz")

    def __repr__(self):
        return '<Quiz %r>' % self.quiz_title


# question model
class Question(db.Model):

    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(500), nullable=False)
    option_one = db.Column(db.String(150), nullable=True)
    option_two = db.Column(db.String(150), nullable=True)
    option_three = db.Column(db.String(150), nullable=True)
    option_four = db.Column(db.String(150), nullable=True)
    answer = db.Column(db.String(150), nullable=True)
    
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'),nullable=False)
    quiz = db.relationship('Quiz',backref=db.backref('quizzes', cascade='all,delete-orphan', lazy=True))
    
    def __repr__(self):
        return '<Question %r>' % self.question_text

        


