from flask import Flask
from app import app

# app=Flask(__name__)
app.config["LOGIN_DISABLED"]=True

def test_student_explore():
    client=app.test_client()


    # Checking GET request
    response=client.get('/student/student_explore')
    assert response.status_code==200
    # Checking if the inserted data is present in form
    assert b'Ongoing' in response.data
    assert b'Data Visualization' in response.data


