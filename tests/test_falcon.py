import pytest
from connexion.apps.falcon_app import FalconApp
from falcon import testing

import conftest

@pytest.fixture()
def client(simple_api_spec_dir):
    app = FalconApp(__name__, specification_dir=simple_api_spec_dir)
    app.add_api('swagger.yaml')
    return testing.TestClient(app.app)


def test_simple(client):
    result = client.simulate_get('/')
    assert result.status_code == 404

    result = client.simulate_get('/v1.0/greeting/hjacobs')
    assert result.status_code == 405

    result = client.simulate_post('/v1.0/greeting/hjacobs')
    assert result.status_code == 200
    assert result.json == {'greeting': 'Hello hjacobs'}
