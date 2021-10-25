# from datetime import datetime

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# def test_Student():
#     app = Flask(__name__)

#     #initializing SQLAlchemy
#     db = SQLAlchemy(app)

#     # app.config['SECRET_KEY'] = '28e1ff6a5cf7255041c3f6917e2b9b98ffc41e107037e6a29b097f72a3f3856f'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.sqlite'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     from app.models.student_details import Student_details

#     db.create_all()
#     db.session.commit()

#     # Adding a sample student details record
#     db.session.add(Student_details(student_id=10, roll_no="CSE_FALL_2021", mobile_num=987, date_of_birth=datetime.strptime("2021-10-24", "%Y-%m-%d").date(), student_bio="Sample bio"))
#     db.session.commit()

#     result=Student_details.query.filter_by(student_id=10).one_or_none()

#     # Deleting the sample record
#     Student_details.query.filter_by(student_id=10).delete()
#     db.session.commit()

#     # Check if record was inserted
#     assert result is not None