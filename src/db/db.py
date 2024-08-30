from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from src.config import settings


engine = create_async_engine(
    url=settings.GET_URL,
    echo=False
)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase): 
    pass
