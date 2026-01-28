from sqlmodel import Field, SQLModel


class SellerUpdate(SQLModel):
    name: str = Field(max_length=200)
    address: str
