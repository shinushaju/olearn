from app import db

class Student_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    student=db.relationship('Student', backref='student_details', cascade='all,delete-orphan')
    roll_no=db.Column(db.String, nullable=False)
    mobile_num = db.Column(db.String, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    student_bio = db.Column(db.String(70))

    def __repr__(self):
        return '<student_details %r>' % self.roll_no