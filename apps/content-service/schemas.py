# Pydantic 스키마 정의
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum

class CategoryEnum(str, Enum):
    EXPERIENCE = "체험"
    HANDMADE = "수공예"
    LOCAL_PRODUCT = "지역상품"

# 콘텐츠 요청/응답 스키마
class ContentBase(BaseModel):
    title: str
    description: str
    image_url: Optional[str]
    location: Optional[str]
    tags: Optional[List[str]] = Field(default_factory=list)
    category: CategoryEnum

class ContentCreate(ContentBase):
    pass

class ContentOut(ContentBase):
    id: int
    creator_id: int
    created_at: datetime | None
    model_config = {
        "from_attributes": True   # ← v2 방식
    }


class ContentUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    location: Optional[str]
    tags: Optional[List[str]]
    image_url: Optional[str]

class Message(BaseModel):
    detail: str