from fastapi import FastAPI
from app.models.seller_model import Seller
from app.core.database import create_db
from app.api.routes import router

app = FastAPI()

app.include_router(router, tags=['Seller'])

@app.on_event("startup")
def on_startup():
    create_db()
