from flask import Flask
from app import app

# app=Flask(__name__)
app.config["LOGIN_DISABLED"]=True

def test_dashboard():
    client=app.test_client()


    # Checking GET request
    response=client.get('/student/dashboard')
    assert response.status_code==200
    # Checking if the inserted data is present in form
    assert b'Explore' in response.data
    assert b'Courses Completed' in response.data


