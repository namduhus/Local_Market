# Pydantic 스키마 정의
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# 콘텐츠 요청/응답 스키마
class ContentBase(BaseModel):
    title: str
    description: str
    image_url: Optional[str]
    location: Optional[str]
    tags: Optional[List[str]] = []

class ContentCreate(ContentBase):
    pass

class ContentOut(ContentBase):
    id: int
    creator_id: int
    created_at: datetime
    model_config = {
        "from_attributes": True   # ← v2 방식
    }
