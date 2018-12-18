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

use_proxy = False

endpoint = "https://python-qa-training.herokuapp.com/api"


def login(email, password):
    path = endpoint + "/auth/login"

    return requests.post(path, json={"email": email, "password": password}, proxies=proxyDict if use_proxy else None,
                         verify=False if use_proxy else None)


def get_issues(token):
    path = endpoint + "/issues"
    headers = {'x-access-token': token}

    return requests.get(path, headers=headers, proxies=proxyDict if use_proxy else None, verify=False if use_proxy
                        else None)


def create_issue(summary, description, priority, token):
    path = endpoint + "/issues"
    headers = {'x-access-token': token}

    return requests.post(path, json={"summary": summary, "description": description, "priority": priority},
                         headers=headers, proxies=proxyDict if use_proxy else None, verify=False if use_proxy else None)
