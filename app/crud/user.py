from sqlalchemy.orm import session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

def create_user(db: session, user_in: UserCreate) -> User:
    db_user = User(
        email = user_in.email,
        hashed_password = hash_password(user_in.password),
        is_active = True
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user