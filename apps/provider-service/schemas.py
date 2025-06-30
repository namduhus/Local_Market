from pydantic import BaseModel

class ProviderCreate(BaseModel):
    name: str
    phone_number: str
    business_name: str
    business_number: str
    password: str

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
