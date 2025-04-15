import pytest
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    return flask_app.test_client()

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Flask API was running!"
