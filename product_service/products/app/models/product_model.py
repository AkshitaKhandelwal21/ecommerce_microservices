from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel


class ProductModel(SQLModel, table=True):
    __tablename__ = "products"

    id: int = Field(primary_key=True)
    name: str = Field(max_length=200, nullable=False)
    desc: str
    price: float = Field(nullable=False)
    # stock_status: bool = Field(foreign_key='', default=True)
    seller_id: int = Field(foreign_key='')
    category: str = Field(foreign_key='')
    sub_category: str = Field(foreign_key='')
    images: List["Image"] = Relationship(back_populates='product')


class Image(SQLModel, table=True):
    __tablename__ = "images"

    id: int | None = Field(primary_key=True)
    url: str
    product_id: int = Field(foreign_key="products.id")
    product: Optional[ProductModel] = Relationship(back_populates="images")
