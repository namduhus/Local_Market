from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import ReviewCreate, ReviewOut
from crud import create_review, get_reviews_by_content
from typing import List
from utils.jwt_handler import get_current_user

router = APIRouter()

# 요청마다 새로운 DB 세션 생성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 리뷰 생성 API
@router.post("/", response_model=ReviewOut)
def create(review: ReviewCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    creator_id= int(current_user)
    return create_review(db, review, user_id=creator_id)  # 임시 user_id (인증 연동 전)

# 콘텐츠별 리뷰 조회 API
@router.get("/content/{content_id}", response_model=List[ReviewOut])
def read_by_content(content_id: int, db: Session = Depends(get_db)):
    return get_reviews_by_content(db, content_id)