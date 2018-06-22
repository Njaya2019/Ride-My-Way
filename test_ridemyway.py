import json
import pytest
from ridemywayEp import app

@pytest.fixture
def client(request):
    test_client=app.test_client()
    return test_client



def test_view_a_ride(client):
    response=client.get('/rides/1')
    assert response.status_code==200