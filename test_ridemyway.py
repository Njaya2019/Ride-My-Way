import json
import pytest
from ridemywayEp import app

@pytest.fixture
def client(request):
    test_client=app.test_client()
    return test_client

def test_make_request(client):
    response=client.post('/rides/1/request')
    assert response.status_code==200

