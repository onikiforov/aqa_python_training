import common_requests
from data.valid_user import ValidUser
from data.invalid_user import InvalidUser


def test_login_valid_credentials():
    response = common_requests.login(ValidUser.email, ValidUser.password)

    assert response.status_code == 200
    assert response.json()['token'] is not None


def test_login_invalid_password():
    response = common_requests.login(ValidUser.email, InvalidUser.password)

    assert response.status_code == 401
    assert response.json()['token'] is None


def test_login_invalid_username():
    response = common_requests.login(InvalidUser.email, ValidUser.password)

    assert response.status_code == 404


def test_login_invalid_credentials():
    response = common_requests.login(InvalidUser.email, InvalidUser.password)

    assert response.status_code == 404


def test_login_empty_fields():
    email = ""
    password = ""

    response = common_requests.login(email, password)

    assert response.status_code == 404
