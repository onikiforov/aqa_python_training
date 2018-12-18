import common_requests

email = "onikiforov@lohika.com"
password = "12345678"


def test_login_valid_credentials():
    response = common_requests.login(email, password)

    assert response.status_code == 200
    assert response.json()['token'] is not None


def test_login_invalid_credentials():
    password = "123456789"

    response = common_requests.login(email, password)

    assert response.status_code == 401
    assert response.json()['token'] is None


def test_login_invalid_username():
    email = "someemail@test.com"

    response = common_requests.login(email, password)

    assert response.status_code == 404


def test_login_empty_fields():
    email = ""
    password = ""

    response = common_requests.login(email, password)

    assert response.status_code == 404
