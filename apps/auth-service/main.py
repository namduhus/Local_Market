from fastapi import FastAPI
from routers import auth
from database import Base, engine

app = FastAPI(title="Auth Service API", description="회원가입 및 로그인을 제공하는 서비스", version="1.0.0")
Base.metadata.create_all(bind=engine)
# 인증 라우터 등록
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])