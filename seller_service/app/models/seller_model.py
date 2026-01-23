from sqlmodel import Column, Field, SQLModel
from sqlmodel import Enum as ENUM
from enum import Enum


class BusinessType(str, Enum):
    INDIVISUAL = "indivisual"
    ORGANIZATION = "organization"
    BRAND = "brand"
 

class Seller(SQLModel):
    id: int = Field(primary_key=True)
    name: str = Field(max_length=200)
    email: str = Field(unique=True, nullable=False)
    phone: str = Field(unique=True)
    address: str
    business_type: str = Field(sa_column=Column(ENUM(BusinessType)))
    verification_status: bool = Field(default=False)
