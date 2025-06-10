from fastapi import FastAPI
from routers import auth
from database import Base, engine

app = FastAPI(title="Auth Service API", version="1.0.0")
Base.metadata.create_all(bind=engine)
# 인증 라우터 등록
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])