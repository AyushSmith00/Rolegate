from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import User
from app.core.config import Settings

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title= "settings.app_name",
    version="settings.app_version",
    debug="settings.debug"

    )

@app.get("/", tags=["Root"])
def root():
    return{"message": "RoleGate API running"}

  
