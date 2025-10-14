from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./recipehub.db"

engine = create_async_engine(
    DATABASE_URL,
    echo=True,       
    future=True
)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
  
    async with SessionLocal() as session:
        yield session
