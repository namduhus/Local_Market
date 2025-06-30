from sqlalchemy.orm import Session
from models import Provider
from schemas import ProviderCreate
from utils import get_password_hash, verify_password

def create_provider(db: Session, provider: ProviderCreate):
    db_provider = Provider(
        name=provider.name,
        phone_number=provider.phone_number,
        business_name=provider.business_name,
        business_number=provider.business_number,
        hashed_password=get_password_hash(provider.password),
    )
    db.add(db_provider)
    db.commit()
    db.refresh(db_provider)
    return db_provider

def authenticate_provider(db: Session, phone_number: str, password: str):
    provider = db.query(Provider).filter(Provider.phone_number == phone_number).first()
    if not provider or not verify_password(password, provider.hashed_password):
        return None
    return provider
