from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate
from utils import hash_password, verify_password
from datetime import datetime

# 사용자 생성
def create_user(db: Session, user: UserCreate):
    db_user = User(
        email=user.email,
        password_hash=hash_password(user.password),
        created_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 사용자 인증
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user