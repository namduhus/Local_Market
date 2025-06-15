# DB 접근 함수 모음 (Create , Read 등)
from sqlalchemy.orm import Session
from models import Content
from schemas import ContentCreate, ContentUpdate
from datetime import datetime
# 콘텐츠 생성
def create_content(db: Session, content: ContentCreate, creator_id: int):
    db_content = Content(
        title=content.title,
        description=content.description,
        image_url=content.image_url,
        location=content.location,
        tags=content.tags or [],  # None 방지
        creator_id=creator_id,
        created_at=datetime.utcnow()
    )
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content

# 전체 콘텐츠 조회
def get_contents(db: Session):
    return db.query(Content).all()

# 특정 콘텐츠 조회
def get_content_by_id(db: Session, content_id: int):
    return db.query(Content).filter(Content.id == content_id).first()


#특정 콘텐츠 수정
def update_content(db: Session, content_id: int, content_data: ContentUpdate):
    content = db.query(Content).filter(Content.id == content_id).first()
    if not content:
        return None
    for key, value in content_data.dict(exclude_unset=True).items():
        setattr(content, key, value)
    db.commit()
    db.refresh(content)
    return content

#특정 콘텐츠 삭제
def delete_content(db: Session, content_id: int):
    content = db.query(Content).filter(Content.id == content_id).first()
    if not content:
        return None
    db.delete(content)
    db.commit()
    return content