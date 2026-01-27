# from fastapi import requests
import requests
from app.models.seller_model import Seller
from app.repositories.seller_repo import Seller_Repository
from app.schemas.seller_create import SellerCreate
from app.services.user_service import UserService


class SellerService():
    
    def create_seller(seller, session, user_id):
        seller_obj = Seller(
            name = seller.name,
            email = seller.email,
            phone = seller.phone,
            address = seller.address,
            business_type = seller.business_type
        )

        data = Seller_Repository.create_seller(seller_obj, session)
        UserService.post_request(user_id)

        return data
