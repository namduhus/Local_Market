# SQLAlchemy 모델 정의
from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, ARRAY
from sqlalchemy.orm import relationship
from database import Base

# 사용자 테이블
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # 사용자 ID
    email = Column(String, unique=True, index=True)     # 이메일
    password_hash = Column(String)                      # 암호화된 비밀번호
    role = Column(String, default="user")              # 역할 (user, creator, admin)
    created_at = Column(TIMESTAMP)                      # 생성일

    contents = relationship("Content", back_populates="creator")  # 등록 콘텐츠

# 콘텐츠 테이블
class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    image_url = Column(String)
    location = Column(String)
    creator_id = Column(Integer, ForeignKey("users.id"))
    tags = Column(ARRAY(String))
    created_at = Column(TIMESTAMP)

    creator = relationship("User", back_populates="contents")