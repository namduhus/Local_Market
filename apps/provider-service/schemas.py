from pydantic import BaseModel, Field
from typing import Optional

class ProviderCreate(BaseModel):
    name: str = Field(description="이름")
    phone_number: str = Field(description="전화번호")
    business_name: str = Field(description="브랜드명")
    business_number: str = Field(description="회사전화번호")
    password: str = Field(description="비밀번호")

class ProviderOut(BaseModel):
    id: int
    name: str
    phone_number: str
    business_name: str
    business_number: str

    model_config = {
        "from_attributes": True   # ← v2 방식
    }

class ProviderLogin(BaseModel):
    phone_number: str
    password: str

#공급자 정보 수정
class ProviderUpdate(BaseModel):
    name: Optional[str]
    phone_number: Optional[str]
    business_name: Optional[str]
    business_number: Optional[str]