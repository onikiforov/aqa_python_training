import pytest
import common_requests
import utils
import json_provider
from data.valid_user import ValidUser
from data.invalid_user import InvalidUser


@pytest.fixture(scope="session", autouse=True)
def client():
    client = common_requests
    return client


@pytest.fixture(scope="session", autouse=True)
def json_p():
    json_p = json_provider
    return json_p


@pytest.fixture(scope="session")
def login(client):
    return client.login(json_provider.login_json(ValidUser.email, ValidUser.password)).json()['token']


@pytest.fixture(scope="session")
def valid_user():
    return ValidUser


@pytest.fixture(scope="session")
def invalid_user():
    return InvalidUser


# Proof of concept fixture that can be parametrized or use default values
@pytest.fixture(scope="session")
def login_test(request, client, valid_user):
    try:
        email = request.param[0]
    except AttributeError:
        email = valid_user.email

    try:
        password = request.param[1]
    except AttributeError:
        password = valid_user.password
    return client.login(json_provider.login_json(email, password)).json()['token']


@pytest.fixture(scope="function")
def create_issue(client, login, request):
    try:
        description = request.param['description']
    except (AttributeError, KeyError):
        description = "create_issue fixture description"

    try:
        summary = request.param['summary']
    except (AttributeError, KeyError):
        summary = "create_issue fixture summary"

    try:
        priority = request.param['priority']
    except (AttributeError, KeyError):
        priority = utils.get_random_priority()

    response = client.create_issue(json_provider.create_issue_json(summary, description, priority), login)
    return response


@pytest.fixture(scope="function")
def delete_issue(create_issue, client, login):
    yield delete_issue
    client.delete_issue(create_issue.json()['_id'], login)
