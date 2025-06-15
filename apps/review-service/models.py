from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import ARRAY
from database import Base
from datetime import datetime

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(Integer)
    user_id = Column(Integer)
    rating = Column(Integer)
    text = Column(Text)
    sentiment = Column(String)
    keywords = Column(ARRAY(String), default=list)  # ✅ 기본값 추가
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)  # ✅ 기본값 추가
