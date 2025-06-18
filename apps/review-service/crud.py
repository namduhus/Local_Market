from sqlalchemy.orm import Session
from models import Review
from schemas import ReviewCreate, ReviewUpdate
from utils.sentiment import analyze_sentiment_with_rating
from utils.keywords import extract_keywords


# 리뷰 생성 함수
def create_review(db: Session, review: ReviewCreate, user_id: int):
    sentiment = analyze_sentiment_with_rating(review.text, review.rating)
    keywords = extract_keywords(review.text)
    db_review = Review(**review.dict(), user_id=user_id, sentiment=sentiment, keywords=keywords)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

# 특정 콘텐츠 ID 기준으로 리뷰 조회 함수
def get_reviews_by_content(db: Session, content_id: int, sort: str = "latest"):
    query = db.query(Review).filter(Review.content_id == content_id)

    if sort == "rating":
        query = query.order_by(Review.rating.desc())
    else:
        query = query.order_by(Review.created_at.desc())

    return query.all()

# 특정 콘텐츠 수정
def update_review(db: Session, review_id: int, review_data: ReviewUpdate):
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        return None
    for key, value in review_data.dict(exclude_unset=True).items():
        setattr(review, key, value)
    db.commit()
    db.refresh(review)
    return review

def delete_review(db: Session, review_id: int):
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        return None
    db.delete(review)
    db.commit()
    return review