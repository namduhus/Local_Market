from enum import Enum
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func,  Enum as SqlEnum
from sqlalchemy.dialects.postgresql import ARRAY
from database import Base
from datetime import datetime

class CategoryEnum(str, Enum):
    EXPERIENCE = "체험"
    HANDMADE = "수공예"
    LOCAL_PRODUCT = "지역상품"
class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    image_url = Column(String)
    location = Column(String)
    creator_id = Column(Integer)
    tags = Column(ARRAY(String), nullable=True)
    category = Column(SqlEnum(CategoryEnum), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False) 