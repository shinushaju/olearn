from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user=db.relationship('User', back_populates='student', cascade='delete')
    name = db.Column(db.String(50), nullable=False)
    roll_no=db.Column(db.String, nullable=True)
    mobile_num = db.Column(db.String, nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    student_bio = db.Column(db.String(70), nullable=True)

    def __repr__(self):
        return '<Student  %r>' % self.name