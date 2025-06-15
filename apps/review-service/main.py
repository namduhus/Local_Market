from fastapi import FastAPI
from routers import review
from database import Base, engine
from fastapi.openapi.utils import get_openapi


app = FastAPI(title="Review Service API", version="1.0.0")

# 개발용: 테이블 자동 생성
Base.metadata.create_all(bind=engine)

# 라우터 등록
app.include_router(review.router, prefix="/reviews", tags=["Reviews"])


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description="리뷰 서비스 API 문서",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", [{"BearerAuth": []}])
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi