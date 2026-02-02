import requests
from django.conf import settings

class APIClient:
    def __init__(self, request=None, token=None):
        self.request = request
        self.base_headers = {"Content-Type": "application/json"}
        if token:
            self.base_headers["Authorization"] = f"Bearer {token}"

    def _get_headers(self):
        headers = {"Content-Type": "application/json"}
        if self.request:
            token = self.request.session.get("auth_token")
            if token: 
                headers["Authorization"] = f"Bearer {token}"

        return headers

    def get(self, url, params=None):
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()

    def post(self, url, data=None):
        return requests.post(url, headers=self._get_headers(), json=data)

    def put(self, url, data=None):
        return requests.put(url, headers=self._get_headers(), json=data)

    def delete(self, url):
        return requests.delete(url, headers=self._get_headers())
    
    # Validation methods
