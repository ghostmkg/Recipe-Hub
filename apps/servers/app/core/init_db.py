import asyncio
from app.core.database import engine
from app.models.base import Base

# Import all your models so they register with Base
from app.models.user import User
from app.models.recipe import Recipe
from app.models.rating import Rating


async def init_db():
    async with engine.begin() as conn:
        # This will create all tables registered on Base
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())
