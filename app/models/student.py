from flask_login import UserMixin
from app import db

# student model here
class Student(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(24), unique=True, nullable=False)
    password = db.Column(db.String(24), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="student")

    def __repr__(self):
        return '<Student %r>' % self.name

    def is_student(self):
        return self.role == 'student'