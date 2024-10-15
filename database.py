from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)# 데이터베이스에 접근하기 위해 필요한 클래스
# create_engine, sessionmaker은 SQLAlchemy 의 규칙
#autocommit=false는 commit을 해야지만 저장 True로 하면 자동 저장 하지만 rollback불가능

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
