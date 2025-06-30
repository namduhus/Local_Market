from fastapi import APIRouter, Depends, HTTPException,  status
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import ProviderCreate, ProviderOut, ProviderLogin, ProviderUpdate
from crud import create_provider, authenticate_provider, update_provider_info
from utils import create_access_token, get_current_provider
from fastapi.security import OAuth2PasswordRequestForm

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
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    provider = authenticate_provider(db, form_data.username, form_data.password)
    if not provider:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": str(provider.id)})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/providers/me", response_model=ProviderOut)
def read_my_provider_info(current_provider=Depends(get_current_provider)):
    return current_provider

@router.patch("/providers/me", response_model=ProviderOut)
def update_my_provider_info(
    updates: ProviderUpdate,
    db: Session = Depends(get_db),
    current_provider=Depends(get_current_provider),
):
    return update_provider_info(db, current_provider, updates)
