import pytest
from addRide import app

@pytest.fixture
def client(request):
    test_client=app.test_client()
    return test_client

def test_add_a_ride(client):
    response=client.post('/rides')
    assert response.status_code==200

