from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import User
from schemas import UserCreate
from utils import hash_password, verify_password

def create_user(db: Session, user: UserCreate) -> User:
    # 중복 체크
    existing = db.query(User).filter(User.nickname == user.nickname).first()
    if existing:
        raise HTTPException(status_code=400, detail="이미 사용 중인 닉네임입니다.")

    # 동일하게 phone_number도 체크 가능
    existing_phone = db.query(User).filter(User.phone_number == user.phone_number).first()
    if existing_phone:
        raise HTTPException(status_code=400, detail="이미 사용 중인 전화번호입니다.")
    hashed_pw = hash_password(user.password)
    new_user = User(
        username=user.username,
        nickname=user.nickname,
        password=hashed_pw,
        phone_number=user.phone_number,
        user_type=user.user_type
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, username: str, password: str) -> User | None:
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        return None
    return user