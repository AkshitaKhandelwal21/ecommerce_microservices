from fastapi import FastAPI

from app.core.database import create_db

app = FastAPI()

@app.on_event('startup')
def on_startup():
    create_db()