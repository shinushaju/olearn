import pytest
from routes import app

def test_course_details():
    ''' Test whether course-details page responds with 200(HTTP OK) status code '''
    response=app.test_client().get('/course-details')
    
    assert response.status_code==200

@pytest.mark.parametrize("route_url", ["", "about", "careers", "contact", "courses", "course-details", "faculty", "login", "programs", "sign-up", "students", "testimonials", "submit", "sturegister", "facregister"])
def test_routes(route_url):
    ''' Test whether all pages respond with 200(HTTP OK) status code '''
    response=app.test_client().get('/'+route_url)
    
    assert response.status_code==200