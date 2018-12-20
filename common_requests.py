import requests

proxy_ip = '127.0.0.1'
proxy_port = '8200'

http_proxy = 'http://{}:{}'.format(proxy_ip, proxy_port)
https_proxy = 'https://{}:{}'.format(proxy_ip, proxy_port)
ftp_proxy = 'ftp://{}:{}'.format(proxy_ip, proxy_port)

proxyDict = {
    'http': http_proxy,
    'https': https_proxy,
    'ftp': ftp_proxy
}

use_proxy = True

base_url = "https://python-qa-training.herokuapp.com/api"
login_endpoint = "/auth/login"
issues_endpoint = "/issues"


def login(email: str, password: str):
    path = base_url + login_endpoint

    return requests.post(path, json={"email": email, "password": password}, proxies=proxyDict if use_proxy else None,
                         verify=False if use_proxy else None)


def get_issues(token):
    path = base_url + issues_endpoint
    headers = {'x-access-token': token}

    return requests.get(path, headers=headers, proxies=proxyDict if use_proxy else None, verify=False if use_proxy
                        else None)


def create_issue(summary, description, priority, token):
    path = base_url + issues_endpoint
    headers = {'x-access-token': token}

    json = {"summary": summary, "description": description, "priority": priority}

    return requests.post(path, json=json, headers=headers, proxies=proxyDict if use_proxy else None,
                         verify=False if use_proxy else None)


def update_issue(token, issue_id, summary=None, description=None, priority=None):
    path = "{}{}/{}".format(base_url, issues_endpoint, issue_id)
    headers = {'x-access-token': token}

    json = {}
    if summary:
        json['summary'] = summary
    if description:
        json['description'] = description
    if priority:
        json['priority'] = priority

    return requests.patch(path, json=json, headers=headers, proxies=proxyDict if use_proxy else None,
                          verify=False if use_proxy else None)


def delete_issue(issue_id, token):
    path = "{}{}/{}".format(base_url, issues_endpoint, issue_id)
    headers = {'x-access-token': token}

    return requests.delete(path, headers=headers, proxies=proxyDict if use_proxy else None,
                          verify=False if use_proxy else None)
