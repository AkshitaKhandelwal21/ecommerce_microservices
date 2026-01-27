from typing import List
from sqlmodel import Field, Relationship, SQLModel

from products.app.models.product_model import Image

class ProductCreate(SQLModel):
    name: str = Field(max_length=200, nullable=False)
    desc: str
    price: float = Field(nullable=False)
    quantity: int = Field(nullable=False)
    category: str = Field(foreign_key='')
    sub_category: str = Field(foreign_key='')
    images: List["Image"] = Relationship(back_populates='product')
    