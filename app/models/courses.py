from app import db
import datetime

# Course Model
class Course(db.Model):

    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(120), nullable=False)
    preview_link = db.Column(db.String(1000), nullable=False)
    course_overview = db.Column(db.String(1000), nullable=False)
    course_skills = db.Column(db.String(720), nullable=False)
    course_duration = db.Column(db.Integer(), nullable=False)
    course_price = db.Column(db.Integer(), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    difficulty_level = db.Column(db.String(150), nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    is_draft = db.Column(db.Boolean, default=True, nullable=False)
    program = db.Column(db.String(150), nullable=False)

    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'),nullable=False)
    faculty = db.relationship('Faculty',backref=db.backref('faculties', cascade='all,delete-orphan', lazy=True))
    sections = db.relationship("Section", back_populates="course")

    def __repr__(self):
        return '<Course %r>' % self.course_name

# Section Model
class Section(db.Model):

    __tablename__ = 'section'

    id = db.Column(db.Integer, primary_key=True)
    section_title = db.Column(db.String(120), nullable=False)
    section_outcome = db.Column(db.String(720), nullable=False)

    course_id = db.Column(db.Integer, db.ForeignKey('course.id'),nullable=False)
    course = db.relationship('Course',backref=db.backref('courses', cascade='all,delete-orphan', lazy=True))
    lectures = db.relationship("Lecture", back_populates="section")

    def __repr__(self):
        return '<Section %r>' % self.section_title

# Lecture Model
class Lecture(db.Model):

    __tablename__ = 'lecture'

    id = db.Column(db.Integer, primary_key=True)
    lecture_title = db.Column(db.String(120), nullable=False)
    lecture_link = db.Column(db.String(1000), nullable=False)
    lecture_duration = db.Column(db.Integer(), nullable=False)

    section_id = db.Column(db.Integer, db.ForeignKey('section.id'),nullable=False)
    section = db.relationship('Section',backref=db.backref('sections', cascade='all,delete-orphan', lazy=True))
    sections = db.relationship("Section", back_populates="lectures")

    def __repr__(self):
        return '<Lecture %r>' % self.lecture_title


