from pydantic import BaseModel
from typing import List, Optional
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
    sentiment: Optional[str]
    keywords: Optional[List[str]]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True  # ORM 객체 직렬화 허용