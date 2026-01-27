import requests
from frontend import settings
from core.api_client import APIClient


PRODUCT_SERVICE_URL = settings.PRODUCT_SERVICE_URL

def get_all_products():
    # response = requests.get(f"{PRODUCT_SERVICE_URL}/products/")
    # response.raise_for_status()
    # return response.json()
    return [
        {"id": 1, "name": "Sample Product 1", "price": 100},
        {"id": 2, "name": "Sample Product 2", "price": 200},
    ]

class ProductService:
    PRODUCT_SERVICE_URL = settings.PRODUCT_SERVICE_URL
    client = APIClient()

    @classmethod
    def get_products(cls):
        print(f"{PRODUCT_SERVICE_URL}/products")
        return cls.client.get(f"{PRODUCT_SERVICE_URL}/products/")

# utils (generalized get method) - each service calls the method with their urls - views 