import pytest


@pytest.fixture(scope="module")
def my_url():
    return "http://srv:5000"


