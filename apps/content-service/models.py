# SQLAlchemy 모델 정의
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ARRAY
from database import Base

# 콘텐츠 테이블
class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    image_url = Column(String)
    location = Column(String)
    creator_id = Column(Integer)  # auth-service와 분리되어 있으므로 ForeignKey 제거
    tags = Column(ARRAY(String))
    created_at = Column(TIMESTAMP)