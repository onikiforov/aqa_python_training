import utils
from data.valid_user import ValidUser


def test_create_issue_valid(login, delete_issue, json_p, client):
    summary = "New test issue {}".format(utils.get_current_timestamp())
    description = "New test issue description"
    priority = utils.get_random_priority()

    response = client.create_issue(json_p.create_issue_json(summary, description, priority), login)

    json = response.json()

    assert response.status_code == 201
    assert json['_id'] is not None
    assert json['description'] == description
    assert json['priority'] == priority
    assert json['created_by'] == ValidUser.username


def test_create_issue_missing_summary(login, json_p, client):
    description = "test_create_issue_missing_summary description"
    priority = utils.get_random_priority()

    response = client.create_issue(json_p.create_issue_json(None, description, priority), login)

    assert response.status_code == 422


def test_create_issue_missing_description(login, json_p, client):
    summary = "test_create_issue_missing_description summary"
    priority = utils.get_random_priority()

    response = client.create_issue(json_p.create_issue_json(summary, None, priority), login)

    assert response.status_code == 422


def test_create_issue_missing_priority(login, json_p, client):
    summary = "test_create_issue_missing_priority summary"
    description = "test_create_issue_missing_priority description"

    response = client.create_issue(json_p.create_issue_json(summary, description, None), login)

    assert response.status_code == 422


def test_create_issue_invalid_priority_min(login, json_p, client):
    summary = "test_create_issue_invalid_priority_min issue"
    description = "test_create_issue_invalid_priority_min description"
    priority = "0"

    response = client.create_issue(json_p.create_issue_json(summary, description, priority), login)

    assert response.status_code == 422


def test_create_issue_invalid_priority_max(login, json_p, client):
    summary = "test_create_issue_invalid_priority_max issue"
    description = "test_create_issue_invalid_priority_max description"
    priority = "6"

    response = client.create_issue(json_p.create_issue_json(summary, description, priority), login)

    assert response.status_code == 422


def test_create_with_invalid_token(json_p, client):
    summary = "test_create_with_invalid_token issue {}".format(utils.get_current_timestamp())
    description = "test_create_with_invalid_token description"
    priority = utils.get_random_priority()

    response = client.create_issue(json_p.create_issue_json(summary, description, priority), token="123")

    # TODO: check with expired token. Expected status code is 401
    assert response.status_code == 500



