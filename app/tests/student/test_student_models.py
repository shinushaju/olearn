# from app import app, db
# from app.models.courses import Course
# from app.models.enrolledCourses import Enrolled_courses
# from app.models.student_details import Student_details
# from app.models.student import Student
# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime

# # Changing the configuration to use test database instead of production database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.sqlite'

# def test_Student():
#     with app.app_context():
#         db.create_all()
        
#         # Inserting record
#         db.session.add(Student(email="sample@sample.com", password=generate_password_hash("SamplePassword"), name="Sample Name"))
#         db.session.commit()

#         # Querying record
#         student=Student.query.filter_by(email="sample@sample.com").one_or_none()
        
#         # Deleting test record
#         Student.query.filter_by(email="sample@sample.com").delete()
#         db.session.commit()

#         # Test cases
#         assert student is not None
#         assert student.email=="sample@sample.com"
#         assert check_password_hash(student.password, "SamplePassword") == True
#         assert student.name=="Sample Name"

# def test_Student_details():
#     with app.app_context():
#         db.create_all()
        
#         # Inserting a sample student details record
#         db.session.add(Student_details(student_id=1, roll_no="CSE_FALL_2021", mobile_num="+91-9876543210", date_of_birth=datetime.strptime("2021-10-24", "%Y-%m-%d").date(), student_bio="Sample bio"))
#         db.session.commit()

#         student_details=Student_details.query.filter_by(student_id=1).one_or_none()

#         # Deleting the sample record
#         Student_details.query.filter_by(student_id=1).delete()
#         db.session.commit()


#         # Test cases
#         assert student_details is not None
#         assert student_details.student_id==1
#         assert student_details.roll_no=="CSE_FALL_2021"
#         assert student_details.mobile_num=="+91-9876543210"
#         assert student_details.date_of_birth==datetime.strptime("2021-10-24", "%Y-%m-%d").date()
#         assert student_details.student_bio=="Sample bio"