# Shared fixture functions.
# Reference: https://docs.pytest.org/en/latest/fixture.html#conftest-py-sharing-fixture-functions
import pytest


@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch('requests.get')
    mock.return_value.__enter__.return_value.json.return_value = {
        'title': 'Lorem Ipsum',
        'extract': 'Lorem ipsum dolor sit amet',
    }
    return mock
