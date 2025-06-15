from pydantic import BaseModel, EmailStr
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

    model_config = {
        "from_attributes": True   # ← v2 방식
    }