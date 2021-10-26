from app import db
from app.models.faculty import Faculty

class Course(db.Model):

    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(120), nullable=False)
    course_overview = db.Column(db.String(1000), nullable=False)
    course_duration = db.Column(db.Integer(), nullable=False)
    course_price = db.Column(db.Integer(), nullable=False)

    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'),nullable=False)
    faculty = db.relationship('Faculty',backref=db.backref('faculties', cascade='all,delete-orphan', lazy=True))
    
    def __repr__(self):
        return '<Course %r>' % self.course_name