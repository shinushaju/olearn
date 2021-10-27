# from datetime import datetime
# from app.models.student_details import Student_details

# from flask import Flask
# from app import app, db

# # app=Flask(__name__)
# app.config["LOGIN_DISABLED"]=True
# # Changing the configuration to use test database instead of production database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

# def test_manage_profile():
#     with app.app_context():
#         db.create_all()
#         client=app.test_client()

#         # Checking POST request
#         response=client.post('/student/student_details/2', data=dict(student_id=2, roll_no="CSE_FALL_2021", mobile_num="+91-9876543210", date_of_birth=datetime.strptime("2021-10-24", "%Y-%m-%d").date(), student_bio="Sample bio"))
#         assert response.status_code==200

#         # Checking GET request
#         response=client.get('/student/student_details/2')
#         assert response.status_code==200

#         # Checking database
#         student_details=Student_details.query.filter_by(student_id=2).one_or_none()

#         # Deleting the sample record
#         Student_details.query.filter_by(student_id=2).delete()
#         db.session.commit()


#         # Test cases
#         assert student_details is not None
#         assert student_details.student_id==2
#         assert student_details.roll_no=="CSE_FALL_2021"
#         assert student_details.mobile_num=="+91-9876543210"
#         assert student_details.date_of_birth==datetime.strptime("2021-10-24", "%Y-%m-%d").date()
#         assert student_details.student_bio=="Sample bio"