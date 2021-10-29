from flask import render_template

from app import app, db
from app.models.courses import Course, Section, Lecture

@app.route('/students/create-dummy-courses')
def createDummyCourses():
    "This function deletes all records in course table and inserts 4 course records."
    db.create_all()
    Course.query.delete()
    Section.query.delete()
    Lecture.query.delete()

    # Creating course
    db.session.add(Course(course_name='Cloud DevOps Engineer', course_overview='Dummy overview - change this in views/student/createDummyCourses.py', course_skills="Sample skills", course_duration=200, course_price=10000, difficulty_level="Sample level", program="Sample program", faculty_id=1))
    # Creating first section
    db.session.add(Section(section_no=1, section_title="Sample section 1", section_outcome="Sample outcome 1", course_id=1))
    # Creating two lectures for section 1
    db.session.add(Lecture(lecture_no=1, lecture_title="Sample lecture 1", lecture_link="https://www.youtube.com/embed/-bFvC1_Utj0", lecture_duration=27, section_id=1))
    db.session.add(Lecture(lecture_no=2, lecture_title="Sample lecture 2", lecture_link="https://www.youtube.com/embed/o_sUNqZtfVQ", lecture_duration=15, section_id=1))
    # Creating seccond section
    db.session.add(Section(section_no=2, section_title="Sample section 2", section_outcome="Sample outcome 2", course_id=1))
    # Creating two lectures for section 2
    db.session.add(Lecture(lecture_no=3, lecture_title="Sample lecture 3", lecture_link="https://www.youtube.com/embed/duRPyHV4P5U", lecture_duration=8, section_id=2))
    db.session.add(Lecture(lecture_no=4, lecture_title="Sample lecture 4", lecture_link="https://www.youtube.com/embed/9pZ2xmsSDdo", lecture_duration=15, section_id=2))

    db.session.commit()

    return "<html><body><h2>4 Dummy courses created</h2></body></html>"

    