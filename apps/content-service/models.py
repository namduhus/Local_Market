from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import ARRAY
from database import Base
from datetime import datetime

class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    image_url = Column(String)
    location = Column(String)
    creator_id = Column(Integer)
    tags = Column(ARRAY(String), nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False) 
