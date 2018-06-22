import pytest
from ViewRides import app

@pytest.fixture
def client(request):
    test_client=app.test_client()
    return test_client

def test_viewRides(client):
    response=client.get('/rides')
    assert response.status_code==200
