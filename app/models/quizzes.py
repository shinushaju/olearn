from app import db

# quiz model
class Quiz(db.Model):
    __tablename__ = 'quiz'
    id = db.Column(db.Integer, primary_key=True)
    quiz_title = db.Column(db.String(120), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'),nullable=False)

    def __repr__(self):
        return '<Quiz %r>' % self.quiz_title