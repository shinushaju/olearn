from app import app

def test_faculty_dashboard():
    response = app.test_client().get('/faculty/dashboard')
    assert response.status_code == 200


def test_faculty_courses():
    response = app.test_client().get('/faculty/courses')
    assert response.status_code == 200


def test_create_course():
    response = app.test_client().get('/course/create')
    assert response.status_code == 200


def test_add_section():
    response = app.test_client().get('/course/sections')
    assert response.status_code == 200


def test_add_lecture():
    response = app.test_client().get('/course/section/lectures')
    assert response.status_code == 200

def test_manage_course(course_id):
    response = app.test_client().get('/course/<course_id>/manage')
    assert response.status_code == 200


def test_manage_lectures(course_id, section_id):
    response = app.test_client().get('/course/<course_id>/section/<section_id>/lectures/manage')
    assert response.status_code == 200


def test_edit_course_info():
    response = app.test_client().get('/course/info/edit')
    assert response.status_code == 200

def test_edit_section_info(course_id, section_id):
    response = app.test_client().get('/course/<course_id>/section/<section_id>/info/edit')
    assert response.status_code == 200


def test_edit_lecture_info(course_id, section_id, lecture_id):
    response = app.test_client().get('/course/<course_id>/section/<section_id>/lecture/<lecture_id>/info/edit')
    assert response.status_code == 200

def test_delete_section(course_id, section_id):
    response = app.test_client().get('/course/<course_id>/section/<section_id>/delete')
    assert response.status_code == 200

def test_delete_lecture(lecture_id):
    response = app.test_client().get('/course/section/lecture/<lecture_id>/delete')
    assert response.status_code == 200


