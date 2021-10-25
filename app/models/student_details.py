from app import db

class student_details(db.model):
    roll_no = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    student=db.relationship('Student', backref='student_details')
    mobile_num = db.Column(db.Integer, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    student_bio = db.Column(db.String(70), nullable=False)

    def __repr__(self):
        return '<student_details %r>' % self.roll_no