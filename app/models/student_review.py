from app import db

# Table to store review by students
class Student_review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id=db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    student=db.relationship('Student', backref='student_review')
    course_id=db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    course=db.relationship('Course', backref='student_review')
    subject=db.Column(db.String(100), nullable=False)
    rating=db.Column(db.Float, nullable=False)
    

    def __repr__(self):
        return f'{self.student.name}: {self.course.course_name}'