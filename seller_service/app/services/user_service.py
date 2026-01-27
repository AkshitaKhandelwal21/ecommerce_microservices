import requests

from app.core.config import settings

class UserService:
    user_service_url = settings.user_service_url

    @classmethod
    def post_request(cls, user_id):
        return requests.post(cls.user_service_url, json={
            'user_id': user_id
        })
        
