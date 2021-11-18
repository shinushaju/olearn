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

    ######################  COURSE       #######################
    db.session.add(Course(course_name="Cloud DevOps Engineer",course_overview="This program provides the skills you need to advance your career as a data engineer and provides training to support your preparation for the industry.", course_skills="Javascript, web development with HTML and CSS, and the Linux Command Line.",course_duration=200,course_price=1999, difficulty_level=" Difficult",program="Apply site reliability engineering principles to a service. Optimize service performance. Implement service monitoring strategies", faculty_id=1))
    db.session.add(Course(course_name='Python Programming', course_overview="Fundamentals of the Python programming language, along with programming best practices.",course_skills="Fundamentals of pyton,Analytical skills",course_duration=100,course_price=999,difficulty_level="Easy",program="Expertise of python, Inspect and understand APIs, open source computer vision library", faculty_id=1))
    db.session.add(Course(course_name='Full Stack Web Development',  course_overview="This program is designed to provide the learner with a solid foundation in probability theory to prepare for the broader study of Data Science with Statistics.",course_skills="Experience writing and testing software with Python or another object-oriented programming language",course_duration=160,course_price=1500,difficulty_level="Intermediate",program="Describe the languages, tools, and data . Create and manage source code for data science. Explaination of data science tools", faculty_id=1))
    db.session.add(Course(course_name='Machine Learning', course_overview="This course will provide you a foundational understanding of machine learning models as well as demonstrate how these models can solve complex problems ", course_skills="Computer Science Fundamentals and Programming. Machine Learning Algorithms",course_duration=72, course_price=599, difficulty_level="Easy",program=". Machine Learning Algorithms. Data Modeling and Evaluation. Natural Language Processing", faculty_id=1))

    ############################   SECTIONS   #############################
    #Cloud DevOps Engineer 
    db.session.add(Section(section_title="What is Cloud Computing ?",section_outcome="",course_id=1))
    db.session.add(Section(section_title="What is Azure DevOps ?",section_outcome="",course_id=1))
    db.session.add(Section(section_title="What is DevOps ?",section_outcome="",course_id=1))
    db.session.add(Section(section_title=" CI/CD pipelines for different deployment strategies",section_outcome="",course_id=1))
    db.session.add(Section(section_title="Deploy Infrastructure as Code",section_outcome="",course_id=1))
    #Python Programming
    db.session.add(Section(section_title="Introduction of Python",section_outcome="",course_id=2))
    db.session.add(Section(section_title="Data Types ",section_outcome="",course_id=2))
    db.session.add(Section(section_title="Operators ",section_outcome="",course_id=2))
    db.session.add(Section(section_title="Control flow and looping",section_outcome="",course_id=2))
    db.session.add(Section(section_title="Functions",section_outcome="",course_id=2))
    #Full Stack Web Development
    db.session.add(Section(section_title="Overview",section_outcome="",course_id=3))
    db.session.add(Section(section_title="HTML and CSS",section_outcome="",course_id=3))
    db.session.add(Section(section_title="Programming with Javascript",section_outcome="",course_id=3))
    db.session.add(Section(section_title="NodeJS Development",section_outcome="",course_id=3))
    db.session.add(Section(section_title="MongoDB",section_outcome="",course_id=3))
    
    #Machine Learning
    db.session.add(Section(section_title="Introduction",section_outcome="",course_id=4))
    db.session.add(Section(section_title="Linear Regression with One Variable",section_outcome="",course_id=4))
    db.session.add(Section(section_title="Linear Regression with Multiple Variables",section_outcome="",course_id=4))
    db.session.add(Section(section_title="Logistic Regression",section_outcome="",course_id=4))
    db.session.add(Section(section_title="Neural Networks: Representation",section_outcome="",course_id=4))

    ###########################   LECTURES   #############################

    #Cloud DevOps Engineer 
    db.session.add(Lecture(lecture_title="Cloud Computing",lecture_link="https://www.youtube.com/embed/M988_fsOSWo",lecture_duration=6,section_id=1))
    db.session.add(Lecture(lecture_title="Azure DevOps",lecture_link="https://www.youtube.com/embed/jRgLSMlp28U",lecture_duration=13,section_id=2))
    db.session.add(Lecture(lecture_title="DevOps Tutorial",lecture_link="https://www.youtube.com/embed/Xrgk023l4lI",lecture_duration=5,section_id=3))
    db.session.add(Lecture(lecture_title=" CI/CD pipelines for different deployment strategies",lecture_link="https://www.youtube.com/embed/k2aNsQKwyOo",lecture_duration=10,section_id=4))
    db.session.add(Lecture(lecture_title="DevOps Infrastructure as Code",lecture_link="https://www.youtube.com/embed/jnxc4-KI0Rg",lecture_duration=12,section_id=5))
       

    #Python Programming
    db.session.add(Lecture(lecture_title="Introduction to Python",lecture_link="https://www.youtube.com/embed/hEgO047GxaQ",lecture_duration=4,section_id=6))
    db.session.add(Lecture(lecture_title="Data Types in Python",lecture_link="https://www.youtube.com/embed/gCCVsvgR2KU",lecture_duration=14,section_id=7))
    db.session.add(Lecture(lecture_title="Operators in Python",lecture_link="https://www.youtube.com/embed/v5MR5JnKcZI",lecture_duration=11,section_id=8))
    db.session.add(Lecture(lecture_title="Control Flow in Python",lecture_link="https://www.youtube.com/embed/Zp5MuPOtsSY",lecture_duration=16,section_id=9))
    db.session.add(Lecture(lecture_title="Functions in Python",lecture_link="https://www.youtube.com/embed/BVfCWuca9nw",lecture_duration=11,section_id=10))
    #Full Stack Web Development
    db.session.add(Lecture(lecture_title="What is full stack web development",lecture_link="https://www.youtube.com/embed/8KaJRw-rfn8",lecture_duration=7,section_id=11))
    db.session.add(Lecture(lecture_title="HTML CSS Tutorial",lecture_link="https://www.youtube.com/embed/QMnv3QrjZoU",lecture_duration=35,section_id=12))
    db.session.add(Lecture(lecture_title="JavaScript",lecture_link="https://www.youtube.com/embed/upDLs1sn7g4",lecture_duration=5,section_id=13))
    db.session.add(Lecture(lecture_title=" Learn Node.js",lecture_link="https://www.youtube.com/embed/p2JmuSzEUdE",lecture_duration=20,section_id=14))
    db.session.add(Lecture(lecture_title="MongoDB",lecture_link="https://www.youtube.com/embed/pWbMrx5rVBE",lecture_duration=32,section_id=15))
    #Machine Learning
    db.session.add(Lecture(lecture_title="Introduction To Machine Learning",lecture_link="https://www.youtube.com/embed/ukzFI9rgwfU",lecture_duration=8,section_id=16))
    db.session.add(Lecture(lecture_title="Linear Regression Single Variable",lecture_link="Linear Regression with One Variable",lecture_duration=15,section_id=17))
    db.session.add(Lecture(lecture_title="Linear Regression Multiple Variables",lecture_link="https://www.youtube.com/embed/J_LnPL3Qg70",lecture_duration=14,section_id=18))
    db.session.add(Lecture(lecture_title="Logistic Regression",lecture_link="https://www.youtube.com/embed/S4IG2wv9Lnk",lecture_duration=12,section_id=19))
    db.session.add(Lecture(lecture_title="NEURAL NETWORK REPRESENTATIONS IN ML",lecture_link="https://www.youtube.com/embed/88hy5VmjxQg",lecture_duration=12,section_id=20))
    
    
    db.session.commit()

    return "<html><body><h2>4 Dummy courses created</h2></body></html>"

    