import requests
from typing import Any


class RequestService:
    def get(self, url, **kwargs):
        return requests.get(url, **kwargs)
    
    def post(self, url, json: Any | None):
        return requests.post(url, json=json)
