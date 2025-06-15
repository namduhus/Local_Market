from fastapi import FastAPI
from routers import content
from database import Base, engine
from fastapi.openapi.utils import get_openapi


app = FastAPI(title="Content Service API", description="콘텐츠 등록, 조회, 상세기능을 제공하는 서비스", version="1.0.0")

# 개발 초기에는 자동 테이블 생성을 위해 사용되며,
# 운영 환경에서는 Alembic 같은 마이그레이션 도구로 대체하는 것이 좋습니다.
Base.metadata.create_all(bind=engine)

# 콘텐츠 라우터 등록
app.include_router(content.router, prefix="/contents", tags=["Contents"])

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description="콘텐츠 서비스 API 문서",
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