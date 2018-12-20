import pytest

from data.invalid_user import InvalidUser
from data.valid_user import ValidUser


@pytest.mark.parametrize("email, password, expected_status_code",
                         [(ValidUser.email, ValidUser.password, 200),
                          (ValidUser.email, InvalidUser.password, 401),
                          (InvalidUser.email, ValidUser.password, 404),
                          (InvalidUser.email, InvalidUser.password, 404),
                          ("", "", 404)])
def test_login(client, email, password, expected_status_code, json_p):
    assert client.login(json_p.login_json(email, password)).status_code == expected_status_code
