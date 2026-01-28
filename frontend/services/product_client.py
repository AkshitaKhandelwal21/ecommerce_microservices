import requests
from frontend import settings
from core.api_client import APIClient


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
    def get_products(cls, params=None):
        return cls.client.get(f"{cls.PRODUCT_SERVICE_URL}/products/", params=params)
    
    @classmethod
    def get_subcat(cls):
        return cls.client.get(f"{cls.PRODUCT_SERVICE_URL}/subcat/")
    
    @classmethod
    def get_category(cls):
        return cls.client.get(f"{cls.PRODUCT_SERVICE_URL}/category/")
    
    @classmethod
    def new_product(cls):
        return cls.client.post(f"{cls.PRODUCT_SERVICE_URL}/products/")
    
    # @classmethod
    # def get_product_by_subcategory(cls, sub):
    #     return cls.client.get(f"{cls.PRODUCT_SERVICE_URL}/product/{sub}")

# utils (generalized get method) - each service calls the method with their urls - views 