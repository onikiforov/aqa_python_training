def test_login_valid_credentials(client, json_p, valid_user):
    response = client.login(json_p.login_json(valid_user.email, valid_user.password))

    assert response.status_code == 200
    assert response.json()['token'] is not None


def test_login_invalid_password(client, json_p, valid_user, invalid_user):
    response = client.login(json_p.login_json(valid_user.email, invalid_user.password))

    assert response.status_code == 401
    assert response.json()['token'] is None


def test_login_invalid_username(client, json_p, valid_user, invalid_user):
    response = client.login(json_p.login_json(invalid_user.email, valid_user.password))

    assert response.status_code == 404


def test_login_invalid_credentials(client, json_p, invalid_user):
    response = client.login(json_p.login_json(invalid_user.email, invalid_user.password))

    assert response.status_code == 404


def test_login_empty_fields(client, json_p):
    email = ""
    password = ""

    response = client.login(json_p.login_json(email, password))

    assert response.status_code == 404
