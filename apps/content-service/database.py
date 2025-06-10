# DB 연결 및 세션 설정
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 데이터베이스 연결 설정
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/content_db")

# SQLAlchemy 세션 및 베이스 설정
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()