import requests


token = ''
mkdir_url = "https://cloud-api.yandex.net/v1/disk/resources"


def create_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': token}
    create_dir = requests.api.put(mkdir_url, headers=headers, params=params)
    return create_dir.status_code


def delete_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': token}
    create_dir = requests.api.delete(mkdir_url, headers=headers, params=params)
    return create_dir.status_code

# create_folder('new')
# delete_folder('new')
