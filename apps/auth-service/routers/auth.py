from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserCreate, UserOut
from crud import create_user, authenticate_user
from database import SessionLocal
from utils import create_access_token
from models import User 
from utils import verify_password
from schemas import LoginRequest
from datetime import timedelta

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/auth/register", response_model=UserOut, summary="회원가입")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.nickname == request.nickname).first()
    
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="토큰이 만료되었습니다.")
    
    access_token_expires = timedelta(minutes=60)
    access_token = create_access_token(
        data={"sub": str(user.id)},  # 또는 email, nickname 등 고유한 값
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "nickname": user.nickname
    }