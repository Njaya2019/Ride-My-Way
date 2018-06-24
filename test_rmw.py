import pytest
from rmw import app

@pytest.fixture
def client(request):
    test_client=app.test_client()
    return test_client

def test_viewRides(client):
    response=client.get('/rides')
    assert response.status_code==200

def test_view_a_ride(client):
    response=client.get('/rides/1')
    assert response.status_code==200

def test_make_request(client):
    response=client.post('/rides/1/request')
    assert response.status_code==200

def test_add_a_ride(client):
    response=client.post('/rides')
    assert response.status_code==200