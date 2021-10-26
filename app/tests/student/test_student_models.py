from app import app, db
from app.models.courses import Course
from app.models.enrolledCourses import Enrolled_courses
from app.models.student_details import Student_details
from app.models.student import Student
from werkzeug.security import generate_password_hash, check_password_hash

def test_student():
    with app.app_context():
        db.create_all()
        
        db.session.add(Student(email="sample@sample.com", password=generate_password_hash("SamplePassword"), name="Sample Name"))
        db.session.commit()

        student=Student.query.filter_by(email="sample@sample.com").one_or_none()
        
        Student.query.filter_by(email="sample@sample.com").delete()
        db.session.commit()

        assert student is not None
        assert student.email=="sample@sample.com"
        assert check_password_hash(student.password, "SamplePassword") == True
        assert student.name=="Sample Name"