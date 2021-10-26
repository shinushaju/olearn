from app import db

# Table to store courses enrolled by students
class student_review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject=db.Column(db.String(100),nullable=False)
    rating=db.Column(db.Integer, nullable=False )
   
    def __repr__(self):
        return f'{self.student.name}: {self.course.course_name}'