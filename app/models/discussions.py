from sqlalchemy.orm import query
from app import db
#from app.models.courses import Course
import datetime
from app.models.faculty import Faculty

###student can create a query and also reply and faculty can only reply 
class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query_text = db.Column(db.String(100), nullable=False)
    query_status = db.Column(db.Boolean, default=False, nullable=False)
    student_name = db.Column(db.String(100),nullable=False)
    course_name = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return '<Query %r>' % self.query_text

'''
class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reply_text = db.Column(db.String(100))
    request_id = db.Column(db.Integer, db.ForeignKey('Query.id'))
    faculty_id = db.Column(db.Integer, db.ForeignKey('Faculty.id'))
    
    # we need foregin keys- course, faculty and student, query, 
    # columns id, reply_text, date and time
    def __repr__(self):
        return '<Course %r>' % self.course_name
'''