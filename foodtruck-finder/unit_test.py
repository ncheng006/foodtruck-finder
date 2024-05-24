import pytest

BASE_URL = "http://localhost:5000"

@pytest.fixture
def client():
    from app import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_foodtrucks(client):
    response = client.get('/api/foodtrucks?lat=37.7749&lon=-122.4194&radius=5')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'name' in data[0]
    assert 'latitude' in data[0]
    assert 'longitude' in data[0]
    assert 'distance' in data[0]

def test_invalid_parameters(client):
    response = client.get('/api/foodtrucks?lat=invalid&lon=invalid&radius=5')
    assert response.status_code == 400


def test_no_food_trucks_in_radius(client):
    response = client.get('/api/foodtrucks?lat=37&lon=-122&radius=0.1')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_missing_parameters(client):
    response = client.get('/api/foodtrucks?lat=37.7749')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Invalid latitude or longitude'

def test_default_radius(client):
    response = client.get('/api/foodtrucks?lat=37.7749&lon=-122.4194')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0