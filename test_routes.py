from routes import app
import pytest

def test_app():
    response = app.test_client().get('/hello')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'
