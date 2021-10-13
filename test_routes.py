from routes import app

def test_course_details():
    response=app.test_client().get('/course-details')
    
    assert response.status_code==200