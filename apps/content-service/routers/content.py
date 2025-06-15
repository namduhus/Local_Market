from utils.jwt_handler import get_current_user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import ContentCreate, ContentOut, ContentUpdate
from crud import create_content, get_contents, get_content_by_id, update_content, delete_content
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
@router.post(path="/content/create", summary="콘텐츠 생성 기능", description="콘텐츠를 생성하는 기능입니다.", tags=["Create"], response_model=ContentOut)
def create(content: ContentCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    creator_id= int(current_user)
    return create_content(db, content, creator_id=creator_id)

# 콘텐츠 전체 조회 API
@router.get(path="/content/search", summary="생성된 콘텐츠 전체 조회 기능", description="생성된 콘텐츠 전체 조회합니다." , tags=["All_Contents"], response_model=List[ContentOut])
def read_all(db: Session = Depends(get_db)):
    return get_contents(db)

# 콘텐츠 상세 조회 API
@router.get(path="/content/{content_id}", summary="특정 콘텐츠 조회 기능", description="조회할 콘텐츠 id 입력", tags=["Select_Contents"], response_model=ContentOut)
def read_one(content_id: int, db: Session = Depends(get_db)):
    content = get_content_by_id(db, content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content

# 콘텐츠 상세 수정 API
@router.put(path="/content/{content_id}/update", summary="특정 콘텐츠 수정 기능", description="수정을 원하는 contents_id 입력",tags=["Update"], response_model=ContentOut)
def update_content_route(content_id: int, content_data: ContentUpdate, db: Session = Depends(get_db)):
    updated = update_content(db, content_id, content_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Content not found")
    return updated

# 콘텐츠 지정삭제 API
@router.delete(path="/content/{content_id}/delete", summary="특정 콘텐츠 삭제 기능", description="삭제를 원하는 contents_id 입력", tags=["Delete"], response_model=ContentOut)
def delete_content_route(content_id: int, db: Session = Depends(get_db)):
    deleted = delete_content(db, content_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Content not found")
    return {"detail": "Content deleted"}