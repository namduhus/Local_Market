from pydantic import BaseModel, constr
from typing import Literal


# 회원가입 요청
class UserCreate(BaseModel):
    username: constr(min_length=3)
    nickname: str
    password: constr(min_length=6)
    phone_number: str
    user_type: Literal["user", "provider"]

# 사용자 응답 스키마
class UserOut(BaseModel):
    id: int
    username: str
    nickname: str
    phone_number: str
    user_type: str

    model_config = {
        "from_attributes": True   # ← v2 방식
    }

class LoginRequest(BaseModel):
    nickname: str
    password: str