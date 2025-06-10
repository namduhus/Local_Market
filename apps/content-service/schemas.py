# Pydantic 스키마 정의
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# 사용자 요청/응답 스키마
class UserBase(BaseModel):
    email: EmailStr
    role: Optional[str] = "user"

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

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
    class Config:
        orm_mode = True
