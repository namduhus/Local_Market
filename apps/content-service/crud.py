# DB 접근 함수 모음 (Create , Read 등)
from sqlalchemy.orm import Session
from models import Content
from schemas import ContentCreate
# 콘텐츠 생성
def create_content(db: Session, content: ContentCreate, creator_id: int):
    db_content = Content(**content.dict(), creator_id=creator_id)
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