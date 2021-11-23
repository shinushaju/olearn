from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_about():
    response = app.test_client().get('/about')
    assert response.status_code == 200

def test_careers():
    response = app.test_client().get('/careers')
    assert response.status_code == 200

def test_courses():
    response = app.test_client().get('/courses')
    assert response.status_code == 200

def test_contact():
    response = app.test_client().get('/contact')
    assert response.status_code == 200

def test_data_science_course():
    response = app.test_client().get('/courses/data-science')
    assert response.status_code == 200

def test_programming_course():
    response = app.test_client().get('/courses/programming')
    assert response.status_code == 200

def test_artificial_intelligence_course():
    response = app.test_client().get('/courses/artificial-intelligence')
    assert response.status_code == 200

def test_blockchain_course():
    response = app.test_client().get('/courses/blockchain')
    assert response.status_code == 200

def test_cloud_computing_course():
    response = app.test_client().get('/courses/cloud-computing')
    assert response.status_code == 200

def test_quantum_computing_course():
    response = app.test_client().get('/courses/quantum_computing')
    assert response.status_code == 200

def test_course_details():
    response = app.test_client().get('/course-details')
    assert response.status_code == 200

def test_faculty():
    response = app.test_client().get('/faculty')
    assert response.status_code == 200

def test_programs():
    response = app.test_client().get('/programs')
    assert response.status_code == 200

def test_students():
    response = app.test_client().get('/students')
    assert response.status_code == 200

def test_testimonials():
    response = app.test_client().get('/testimonials')
    assert response.status_code == 200

def test_sign_up():
    response = app.test_client().get('/sign-up')
    assert response.status_code == 200

def test_login():
    response = app.test_client().get('/login')
    assert response.status_code == 200

