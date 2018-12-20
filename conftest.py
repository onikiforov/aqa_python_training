import pytest

import common_requests
from data.valid_user import ValidUser


@pytest.fixture(scope="session", autouse=True)
def client():
    client = common_requests
    return client


@pytest.fixture(scope="session")
def login(client):
    return client.login(ValidUser.email, ValidUser.password).json()['token']


# WIP fixture to fetch user data
@pytest.fixture(scope="session")
def user():
    pass


# Proof of concept fixture that can be parametrized or use default values
@pytest.fixture(scope="session")
def login_test(request, client):
    try:
        email = request.param[0]
    except AttributeError:
        email = "onikiforov@lohika.com"

    try:
        password = request.param[1]
    except AttributeError:
            password = "12345678"
    return client.login(email, password).json()['token']


@pytest.fixture(scope="function")
def delete_issue(request, client, login):
    yield delete_issue
    print(request.param[0])
    client.delete_issue(request.param.json()['_id'], login)
