import os

import requests
import base64

from OutputExport import OutputExport


def repository_request():
    github_token = os.environ['GITHUB_TOKEN']
    github_owner = os.environ['GITHUB_OWNER']
    github_repo = os.environ['GITHUB_REPO']
    headers = {
        'Authorization': f'Bearer {github_token}',
        'Accept': 'application/vnd.github+json'
        # 'Accept': 'application/vnd.github.raw+json'
        # 'Accept': 'application/json'
    }
    url = f'https://api.github.com/repos/{github_owner}/{github_repo}/contents/bubble_sort.cpp'
    response = requests.get(url=url, headers=headers, verify=False)
    if response.ok:
        body = response.json()
        content: str = body['content']
        filename = body['name']
        # OutputExport.export_to_json(content=response.json(), filename="response")
        OutputExport.export_bytes(content=base64.b64decode(content), filename=filename)

        # for directory get the raw content. Header 'application/vnd.github.raw+json' must be set.
        # OutputExport.export_bytes(content=response.content, filename="response")
        print(">>> Success!")
    else:
        print(response.json())
        raise requests.HTTPError

def repository_tree():
    github_token = os.environ['GITHUB_TOKEN']
    github_owner = os.environ['GITHUB_OWNER']
    github_repo = os.environ['GITHUB_REPO']
    headers = {
        'Authorization': f'Bearer {github_token}',
        'Accept': 'application/vnd.github+json'
    }
    url = f'https://api.github.com/repos/{github_owner}/{github_repo}/git/trees/main?recursive=true'
    response = requests.get(url=url, headers=headers, verify=False)
    if response.ok:
        OutputExport.export_to_json(content=response.json(), filename="tree")
        print(">>> Tree Success!")


if __name__ == '__main__':
    # repository_request()
    repository_tree()
