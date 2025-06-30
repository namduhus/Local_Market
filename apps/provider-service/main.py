from fastapi import FastAPI
from routers import provider
from database import Base, engine

app = FastAPI(title="Provider Service API", description="공급자 회원가입 및 로그인을 제공하는 서비스", version="1.0.0")

Base.metadata.create_all(bind=engine)

app.include_router(provider.router)
