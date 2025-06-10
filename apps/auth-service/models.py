from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base

# 사용자 테이블 정의
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # 사용자 ID
    email = Column(String, unique=True, index=True)     # 이메일 주소
    password_hash = Column(String)                      # 해시된 비밀번호
    role = Column(String, default="user")              # 사용자 역할
    created_at = Column(TIMESTAMP)                      # 가입 일자
