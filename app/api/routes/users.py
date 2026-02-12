from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import session

from app.schemas.user import UserCreate, UserOut
from app.crud.user import create_user
from app.db.deps import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserOut)

def register_user(
    user_in: UserCreate,
    db: session = Depends(get_db)):
    try: 
        return create_user(db, user_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))