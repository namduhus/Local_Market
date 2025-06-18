from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime

# 리뷰 생성 요청 스키마
class ReviewCreate(BaseModel):
    content_id: int
    rating: int
    text: str

# 리뷰 응답 스키마
class ReviewOut(ReviewCreate):
    id: int
    user_id: int
    rating: int
    text: str
    sentiment: Optional[str]
    keywords: Optional[List[str]] = Field(default_factory=list)
    created_at: Optional[datetime]

    model_config = {
        "from_attributes": True   # ← v2 방식
    }

class ReviewUpdate(BaseModel):
    text: Optional[str]
    rating: Optional[int]

class Message(BaseModel):
    detail: str

class ReviewStats(BaseModel):
    content_id: int
    average_rating: float
    review_count: int
    sentiment_distribution: Dict[str, int]