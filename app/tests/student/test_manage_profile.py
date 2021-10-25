from datetime import datetime

from flask import Flask
from app import app

# app=Flask(__name__)
app.config["LOGIN_DISABLED"]=True

def test_manage_profile():
    client=app.test_client()

    # Checking POST request
    response=client.post('/student/student_details/1', data=dict(student_id=1, roll_no="CSE_FALL2021", mobile_num="9876564537", date_of_birth=datetime.strptime("2021-10-24", "%Y-%m-%d").date(), student_bio="Sample bio"))
    assert response.status_code==200
    assert b'Successful' in response.data

    # Checking GET request
    response=client.get('/student/student_details/1')
    assert response.status_code==200
    # Checking if the inserted data is present in form
    assert b'CSE_FALL2021' in response.data