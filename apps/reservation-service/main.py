# main.py
from fastapi import FastAPI
from routers import reservation  
from fastapi.openapi.utils import get_openapi

app = FastAPI(title="Reservation Service API", description="예약등록 및 조회 담당하는 서비스.",version="1.0.0")

# 라우터 등록
app.include_router(reservation.router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Reservation Service",
        version="1.0.0",
        description="예약 서비스 API 문서",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            if "security" not in openapi_schema["paths"][path][method]:
                openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi