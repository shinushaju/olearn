from sqlalchemy.orm import query
from app import db
#from app.models.courses import Course
import datetime
from app.models.faculty import Faculty

###student can create a query and also reply and faculty can only reply 
class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query_title = db.Column(db.String(100), nullable=False)
    query_text = db.Column(db.String(500), nullable=False)
    # query_status = db.Column(db.Boolean, default=False, nullable=False)
    # student_name = db.Column(db.String(100),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship('User', back_populates='queries', cascade='delete')
    # course_name = db.Column(db.String(100), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    course = db.relationship('Course', back_populates='queries', cascade='delete')
    created_on = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    replies = db.relationship('Reply', back_populates='query')
    
    def __repr__(self):
        return '<Query %r>' % self.query_text


class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query_id=db.Column(db.Integer, db.ForeignKey("query.id"), nullable=False)
    query=db.relationship('Query', back_populates='replies', cascade='delete')
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user=db.relationship('User', back_populates='replies', cascade='delete')
    reply_text = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    # faculty_id = db.Column(db.Integer)
    
    # we need foregin keys- course, faculty and student, query, 
    # columns id, reply_text, date and time
    def __repr__(self):
        return '<Reply %r>' % self.reply_text
