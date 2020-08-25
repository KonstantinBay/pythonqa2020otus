import requests


class APIClient:

    def __init__(self, base_path):
        self.base_path = base_path

    def make_url(self, path):
        return '/'.join([self.base_path, path])

    def post(self, path=None, params=None, json=None, headers=None):
        url = self.make_url(path)
        return requests.post(url=url, params=params, json=json, headers=headers)

    def get(self, path=None, params=None):
        url = self.make_url(path)
        return requests.get(url=url, params=params)
