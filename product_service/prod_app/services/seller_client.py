import requests

from products import settings
# from django.conf import settings

class SellerClient:
    BASE_URL = settings.SELLER_SERVICE_URL

    @classmethod
    def get_seller(cls, user_id): 
        response = requests.get(f"{cls.BASE_URL}/seller/{user_id}")
        return response.json()
    
