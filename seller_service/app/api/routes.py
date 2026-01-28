from fastapi import APIRouter, Depends

from app.services.seller_service import SellerService
from app.schemas.seller_create import SellerCreate
from app.core.database import SessionDep
from app.core.security import get_current_user

router = APIRouter()

@router.post('/new_seller')
def create_seller(seller: SellerCreate, session: SessionDep, user_id: int = Depends(get_current_user)):
    SellerService.create_seller(seller, session, user_id)


@router.get('/seller/{id}')
def get_seller_by_user_id(session: SessionDep, user_id: int = Depends(get_current_user)):
    SellerService.get_seller(session, user_id)
