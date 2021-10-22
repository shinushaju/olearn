from app import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(120), nullable=False)
    course_description = db.Column(db.String(720), nullable=False)
    course_duration = db.Column(db.Integer(), nullable=False)
    course_price = db.Column(db.Integer(), nullable=False)
    
    def __repr__(self):
        return '<Course %r>' % self.course_name