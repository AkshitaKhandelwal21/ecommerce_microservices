from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine, SQLModel

db_url = "sqlite:///sellers.db"

engine = create_engine(db_url, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)
    print("DB tables created")
 
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]