from app.core.database import SessionDep


class Seller_Repository():
    
    def create_seller(data, session):
        session.add(data)
        session.commit()
        session.refresh(data)
        return data