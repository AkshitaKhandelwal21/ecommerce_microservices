from sqlmodel import Column, Field, SQLModel
from sqlmodel import Enum as ENUM

from app.models.seller_model import BusinessType

class SellerCreate(SQLModel):
    name: str = Field(max_length=200)
    email: str = Field(unique=True, nullable=False)
    phone: str = Field(unique=True)
    address: str
    business_type: str = Field(sa_column=Column(ENUM(BusinessType)))