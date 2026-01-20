import requests
from frontend import settings


PRODUCT_SERVICE_URL = settings.PRODUCT_SERVICE_URL

def get_all_products():
    # response = requests.get(f"{PRODUCT_SERVICE_URL}/products/")
    # response.raise_for_status()
    # return response.json()
    return [
        {"id": 1, "name": "Sample Product 1", "price": 100},
        {"id": 2, "name": "Sample Product 2", "price": 200},
    ]


# utils (generalized get method) - each service calls the method with their urls - views 