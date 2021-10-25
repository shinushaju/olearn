from app import db

class student_details(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False, primary_key=True)
    student=db.relationship('Student', backref='student_details')
    roll_no=db.Column(db.String, nullable=False)
    mobile_num = db.Column(db.Integer, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    student_bio = db.Column(db.String(70))

    def __init__(self, **kwargs):
        self.student_id=kwargs.get('student_id')
        self.roll_no=kwargs.get('roll_no')
        self.mobile_num=kwargs.get('mobile_num')
        self.date_of_birth=kwargs.get('date_of_birth')
        self.student_bio=kwargs.get('student_bio')


    def __repr__(self):
        return '<student_details %r>' % self.roll_no