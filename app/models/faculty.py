from flask_login import UserMixin
from app import db

# Faculty Model
class Faculty(UserMixin, db.Model):

    __tablename__ = 'faculty'

    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(24), unique=True, nullable=False)
    password = db.Column(db.String(24), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return '<Faculty %r>' % self.name

    def is_faculty(self):
        return self.role == 'faculty'
