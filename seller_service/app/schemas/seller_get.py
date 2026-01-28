from sqlmodel import Field, SQLModel


class SellerRead(SQLModel):
    name: str = Field(max_length=200)
    email: str = Field(unique=True, nullable=False)
    phone: str = Field(unique=True)
    address: str
