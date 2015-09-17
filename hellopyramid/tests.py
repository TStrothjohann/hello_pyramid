import pytest
from pyramid import testing

@pytest.fixture
def pyramid_req():
    return testing.DummyRequest()


def test_my_view(pyramid_req):
    from views import my_view
    response = my_view(pyramid_req)
    assert response['greeting'] == 'Hello world!'