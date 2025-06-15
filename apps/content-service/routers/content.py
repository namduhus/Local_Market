from utils.jwt_handler import get_current_user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import ContentCreate, ContentOut
from crud import create_content, get_contents, get_content_by_id
from typing import List

router = APIRouter()

# DB 세션 종속성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 콘텐츠 생성 API
@router.post("/", response_model=ContentOut)
def create(content: ContentCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    creator_id= int(current_user)
    return create_content(db, content, creator_id=creator_id)

# 콘텐츠 전체 조회 API
@router.get("/", response_model=List[ContentOut])
def read_all(db: Session = Depends(get_db)):
    return get_contents(db)

# 콘텐츠 상세 조회 API
@router.get("/{content_id}", response_model=ContentOut)
def read_one(content_id: int, db: Session = Depends(get_db)):
    content = get_content_by_id(db, content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content