from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ARRAY
from database import Base

# 리뷰 테이블 정의
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)         # 리뷰 ID
    content_id = Column(Integer)                               # 연결된 콘텐츠 ID
    user_id = Column(Integer)                                  # 작성자 ID
    rating = Column(Integer)                                   # 별점 (1~5)
    text = Column(Text)                                        # 리뷰 본문
    sentiment = Column(String)                                 # 감정 분석 결과
    keywords = Column(ARRAY(String))                           # 추출된 키워드 리스트
    created_at = Column(TIMESTAMP)                             # 리뷰 작성 시간