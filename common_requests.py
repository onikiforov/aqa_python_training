import requests

# Proxy setup, used for debugging
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

use_proxy = False

base_url = "https://python-qa-training.herokuapp.com/api"
login_endpoint = "/auth/login"
issues_endpoint = "/issues"


def login(json: dict):
    path = base_url + login_endpoint

    return requests.post(path, json=json, proxies=[None, proxyDict][use_proxy], verify=[None, False][use_proxy])


def get_issues(token):
    path = base_url + issues_endpoint
    headers = {'x-access-token': token}

    return requests.get(path, headers=headers, proxies=[None, proxyDict][use_proxy], verify=[None, False][use_proxy])


def create_issue(json: dict, token):
    path = base_url + issues_endpoint
    headers = {'x-access-token': token}

    return requests.post(path, json=json, headers=headers, proxies=[None, proxyDict][use_proxy],
                         verify=[None, False][use_proxy])


# Not sure about passing None values as default
def update_issue(token, issue_id: str, json: dict):
    path = "{}{}/{}".format(base_url, issues_endpoint, issue_id)
    headers = {'x-access-token': token}

    return requests.patch(path, json=json, headers=headers, proxies=[None, proxyDict][use_proxy],
                          verify=[None, False][use_proxy])


def delete_issue(issue_id: str, token):
    path = "{}{}/{}".format(base_url, issues_endpoint, issue_id)
    headers = {'x-access-token': token}

    return requests.delete(path, headers=headers, proxies=[None, proxyDict][use_proxy], verify=[None, False][use_proxy])
