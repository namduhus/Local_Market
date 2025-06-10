from fastapi import FastAPI
from routers import content
from database import Base, engine

app = FastAPI(title="Content Service API", version="1.0.0")

# 개발 초기에는 자동 테이블 생성을 위해 사용되며,
# 운영 환경에서는 Alembic 같은 마이그레이션 도구로 대체하는 것이 좋습니다.
Base.metadata.create_all(bind=engine)

# 콘텐츠 라우터 등록
app.include_router(content.router, prefix="/contents", tags=["Contents"])