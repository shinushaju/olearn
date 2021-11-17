from flask_login import UserMixin
from app import db

# Faculty Model
class Faculty(UserMixin, db.Model):

    __tablename__ = 'faculty'

    id = db.Column(db.Integer, primary_key=True) 
    faculty_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Faculty %r>' % self.faculty_id

