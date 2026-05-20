<<<<<<< HEAD
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"

engine = create_async_engine(
=======
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(
>>>>>>> 09fc101 (Fifth Tutorial - Finished)
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

<<<<<<< HEAD
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
=======
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
>>>>>>> 09fc101 (Fifth Tutorial - Finished)


class Base(DeclarativeBase):
    pass


<<<<<<< HEAD
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
=======
def get_db():
    with SessionLocal() as db:
        yield db
>>>>>>> 09fc101 (Fifth Tutorial - Finished)
