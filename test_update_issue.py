import pytest
import utils


@pytest.mark.parametrize('create_issue', [
    ({"description": "test_update_summary_priority description", "summary": "test_update_summary_priority summary"})
], indirect=True)
def test_update_summary_priority(client, login, delete_issue, create_issue, json_p):
    issue_id = create_issue.json()['_id']

    summary = "updated summary for test_update_summary_priority"

    old_priority = create_issue.json()['priority']
    new_priority = old_priority

    while new_priority == old_priority:
        new_priority = utils.get_random_priority()

    response = client.update_issue(login, issue_id, json_p.create_issue_json(summary=summary, priority=new_priority))

    assert response.status_code == 200
    assert response.json()['summary'] == summary
    assert response.json()['priority'] == new_priority
    assert response.json()['date_updated'] != response.json()['date_created']
