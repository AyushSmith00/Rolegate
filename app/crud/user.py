from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password


def create_user(db: Session, user_in: UserCreate) -> User:
    db_user = User(
        email = user_in.email,
        hashed_password = hash_password(user_in.password),
        is_active = True
    )

    db.add(db_user)

    try:
        db.commit()
        db.refresh()
        return db_user
    
    except IntegrityError:
        db.rollback()
        raise ValueError("Email already registered")

def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None
    
    if not verify_password(password, user.hashed_password):
        return None
    
    return user