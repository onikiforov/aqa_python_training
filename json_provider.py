def login_json(email: str, password: str):
    return {"email": email, "password": password}


def create_issue_json(summary=None, description=None, priority=None):
    # Kinda tricky way to exclude null keys from json. If I simply create json, while passing None as a value,
    # corresponding key is sent as null

    json = {}
    if summary:
        json['summary'] = summary
    if description:
        json['description'] = description
    if priority:
        json['priority'] = priority

    return json
