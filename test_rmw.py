import pytest
from rmw import app

client=app.test_client()
   

def test_viewRides():
    response=client.get('/ridesOffered')
    assert response.status_code==200

def test_view_a_ride():
    response=client.get('/rides/1')
    assert response.status_code==200

def test_make_request():
    response=client.post('/rides/1/request')
    assert response.status_code==200

def test_add_a_ride():
    response=client.post('/rides')
    assert response.status_code==200