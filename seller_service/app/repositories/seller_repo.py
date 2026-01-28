from app.core.database import SessionDep
from app.models.seller_model import Seller


class Seller_Repository:
    
    @staticmethod
    def create_seller(data, session):
        session.add(data)
        session.commit()
        session.refresh(data)
        return data
    
    @staticmethod
    def get_user_by_id(user_id: int, session):
        return session.query(Seller).filter(Seller.user_id == user_id).first()
    
    
