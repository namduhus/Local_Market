from fastapi import FastAPI
from routers import review
from database import Base, engine

app = FastAPI(title="Review Service API", version="1.0.0")

# 개발용: 테이블 자동 생성
Base.metadata.create_all(bind=engine)

# 라우터 등록
app.include_router(review.router, prefix="/reviews", tags=["Reviews"])