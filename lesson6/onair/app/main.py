import os
import logging
import faker
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)

from .config import DB_URI
from .models import Base
from .user_repository import get_all_users, make_user

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

fake = faker.Faker()

DB_ECHO = os.environ.get("DB_ECHO", "false").lower() == "true"


def get_engine() -> AsyncEngine:
    return create_async_engine(
        DB_URI,
        echo=DB_ECHO,
    )


def make_session_class(engine: AsyncEngine) -> type[AsyncSession]:
    return async_sessionmaker(
        engine,
        expire_on_commit=False,
    )


async def create_tables(engine: AsyncEngine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables(engine: AsyncEngine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def main():
    engine = get_engine()
    session_klass = make_session_class(engine)

    await create_tables(engine)

    async with session_klass() as session:
        logger.info("Creating users")
        for _ in range(10):
            user = make_user(fake.name(), fake.random_int(18, 100))
            session.add(user)

        await session.flush()
        await session.commit()

    async with session_klass() as session:
        logger.info("Fetching users")
        for user in await get_all_users(session):
            print(user)

    await drop_tables(engine)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
