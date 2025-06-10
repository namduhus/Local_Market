from sqlalchemy.orm import Session
from models import Review
from schemas import ReviewCreate

# 리뷰 생성 함수
def create_review(db: Session, review: ReviewCreate, user_id: int):
    db_review = Review(**review.dict(), user_id=user_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

# 특정 콘텐츠 ID 기준으로 리뷰 조회 함수
def get_reviews_by_content(db: Session, content_id: int):
    return db.query(Review).filter(Review.content_id == content_id).all()