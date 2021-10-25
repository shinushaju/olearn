from app import db

# quiz model
class Quiz(db.Model):

    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True)
    quiz_title = db.Column(db.String(120), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'),nullable=False)

    def __repr__(self):
        return '<Quiz %r>' % self.quiz_title


# question model
class Question(db.Model):

    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    question_no = db.Column(db.Integer, nullable=False)
    question_text = db.Column(db.String(500), nullable=False)
    option_one = db.Column(db.String(150), nullable=True)
    option_two = db.Column(db.String(150), nullable=True)
    option_three = db.Column(db.String(150), nullable=True)
    option_four = db.Column(db.String(150), nullable=True)
    answer = db.Column(db.String(150), nullable=True)
    
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'),nullable=False)
    quiz = db.relationship('Quiz',backref=db.backref('questions', cascade='all,delete-orphan', lazy=True))
    
    def __repr__(self):
        return '<Question %r>' % self.question_text

        


