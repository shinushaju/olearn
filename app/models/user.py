from flask_login import UserMixin
from app import db

# Faculty Model
class User(UserMixin, db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(24), unique=True, nullable=False)
    password = db.Column(db.String(24), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    # one to one relationship with model faculty
    faculty = db.relationship("Faculty", back_populates="user", uselist=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def is_faculty(self):
        return self.role == 'faculty'
