from app import db

# Table to store courses enrolled by students
class Enrolled_courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id=db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    student=db.relationship('Student', backref='enrolled_courses', cascade='delete')
    course_id=db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    course=db.relationship('Course', backref='enrolled_courses', cascade='delete')
    # progress=db.Column(db.Integer, nullable=False)
    completed_sections=db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f'{self.student.name}: {self.course.course_name}'