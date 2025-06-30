from sqlalchemy.orm import Session
from models import Provider
from schemas import ProviderCreate, ProviderUpdate
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

def get_provider_by_business_name(db: Session, business_name: str):
    return db.query(Provider).filter(Provider.business_name == business_name).first()

def update_provider_info(db: Session, provider: Provider, updates: ProviderUpdate):
    db_provider = db.query(Provider).filter(Provider.id == provider.id).first()
    if updates.name:
        db_provider.name = updates.name
    if updates.phone_number:
        db_provider.phone_number = updates.phone_number
    if updates.business_name:
        db_provider.business_name = updates.business_name
    if updates.business_number:
        db_provider.business_number = updates.business_number
    db.commit()
    db.refresh(db_provider)
    return db_provider