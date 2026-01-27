import requests
from django.conf import settings

class APIClient:
    def __init__(self, token=None):
        self.base_headers = {"Content-Type": "application/json"}
        if token:
            self.base_headers["Authorization"] = f"Bearer {token}"

    def get(self, url, params=None):
        return requests.get(url, headers=self.base_headers, params=params)

    def post(self, url, data=None):
        return requests.post(url, headers=self.base_headers, json=data)

    def put(self, url, data=None):
        return requests.put(url, headers=self.base_headers, json=data)

    def delete(self, url):
        return requests.delete(url, headers=self.base_headers)
    
    # Validation methods
