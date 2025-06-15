from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends, Request
import os

# 환경 변수에서 SECRET_KEY 불러오기
SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
ALGORITHM = "HS256"

# JWT 토큰 디코딩 함수
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]  # 일반적으로 이메일
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

# 요청 헤더에서 Bearer 토큰 추출하고 검증하는 함수
def get_current_user(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization header missing")
    token = auth_header.split(" ")[1]
    return verify_token(token)