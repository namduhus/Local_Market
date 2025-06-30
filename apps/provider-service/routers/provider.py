from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import ProviderCreate, ProviderOut, ProviderLogin
from crud import create_provider, authenticate_provider
from utils import create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/providers/register", response_model=ProviderOut)
def register(provider: ProviderCreate, db: Session = Depends(get_db)):
    return create_provider(db, provider)

@router.post("/providers/login")
def login(credentials: ProviderLogin, db: Session = Depends(get_db)):
    provider = authenticate_provider(db, credentials.phone_number, credentials.password)
    if not provider:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": str(provider.id)})
    return {"access_token": access_token, "token_type": "bearer"}
