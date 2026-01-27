from fastapi import APIRouter

from app.services.seller_service import SellerService
from app.schemas.seller_create import SellerCreate
from app.core.database import SessionDep

router = APIRouter()

@router.post('/new_seller')
def create_seller(seller: SellerCreate, session: SessionDep, user_id: int):
    SellerService.create_seller(seller, session, user_id)