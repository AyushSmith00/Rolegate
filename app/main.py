from fastapi import FastAPI
from app.api.routes import users
from app.api.routes import auth

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


  
