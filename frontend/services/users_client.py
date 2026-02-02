from core.api_client import APIClient
from frontend import settings


class UserService:
    # def __init__(self):   
    AUTH_SERVICE_URL = settings.AUTH_SERVICE_URL
    client = APIClient()

    @classmethod
    def register_user(cls, data):
        return cls.client.post(f"{cls.AUTH_SERVICE_URL}/auth/signup/", data)
    
    @classmethod
    def login_user(cls, data):
        return cls.client.post(f"{cls.AUTH_SERVICE_URL}/auth/login/", data)
    
    @classmethod
    def get_profile(cls, request):
        return cls.client.get(f"{cls.AUTH_SERVICE_URL}/users/me")