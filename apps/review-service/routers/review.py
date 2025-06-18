from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import ReviewCreate, ReviewOut, ReviewUpdate, Message
from crud import create_review, get_reviews_by_content, update_review, delete_review
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
@router.post(path="/review/create", summary="리뷰 생성 기능", description="리뷰할 contents_id 및 평점, 텍스트를 입력", tags=["Review"], response_model=ReviewOut)
def create(review: ReviewCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    creator_id= int(current_user)
    return create_review(db, review, user_id=creator_id)  

# 콘텐츠별 리뷰 조회 API
@router.get(path="/review/{content_id}", summary="작성한 리뷰 조회", description="작성한 리뷰 contents_id 입력 (정렬 옵션, latest, rating)", tags=["Search"], response_model=List[ReviewOut])
def read_by_content(content_id: int, sort: str = Query("latest", enum=["latest", "rating"]),db: Session = Depends(get_db)):
    return get_reviews_by_content(db, content_id, sort)

# 콘텐츠별 리뷰 수정
@router.put("/review/{review_id}/update", response_model=ReviewOut)
def update_review_route(review_id: int, review_data: ReviewUpdate, db: Session = Depends(get_db)):
    updated = update_review(db, review_id, review_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Review not found")
    return updated

#콘텐츠별 리뷰 삭제
@router.delete("/review/{review_id}/delete", response_model=Message)
def delete_review_route(review_id: int, db: Session = Depends(get_db)):
    deleted = delete_review(db, review_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return {"detail": "Review deleted"}