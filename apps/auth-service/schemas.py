from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# 회원가입 요청
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# 사용자 응답 스키마
class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        orm_mode = True