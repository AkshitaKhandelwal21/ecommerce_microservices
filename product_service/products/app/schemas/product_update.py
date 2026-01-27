from typing import List
from sqlmodel import Field, Relationship, SQLModel

from products.app.models.product_model import Image

class ProductCreate(SQLModel):
    name: str = Field(max_length=200, nullable=False)
    desc: str
    price: float = Field(nullable=False)
    images: List["Image"] = Relationship(back_populates='product')