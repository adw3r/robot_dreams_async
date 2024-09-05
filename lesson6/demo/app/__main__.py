from contextlib import asynccontextmanager
import logging
import asyncio
from typing import AsyncGenerator

import faker
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)

from . import config
from .user_repository import (
    get_all_users_with_addresses,
    make_address,
    make_user,
)

logging.basicConfig(level=logging.INFO)
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
logger = logging.getLogger(__name__)

fake = faker.Faker()


def engine():
    return create_async_engine(
        config.DB_URI,
        echo=False,
    )


@asynccontextmanager
async def make_session(
    engine: AsyncEngine,
) -> AsyncGenerator[AsyncSession, None]:
    session_factory = async_sessionmaker(engine)
    async with session_factory() as session:
        yield session


async def main():
    logger.info("Hello, World!")

    async with make_session(engine()) as session:
        for i in range(10):
            logger.info(f"Creating user {i}")
            user = make_user(fake.name(), fake.random_int(1, 100))
            address = make_address(
                user, fake.street_address(), fake.city(), fake.country()
            )
            session.add_all([user, address])

        await session.commit()

        for i, user in enumerate(await get_all_users_with_addresses(session)):
            logger.info([i, user, user.addresses])


if __name__ == "__main__":
    asyncio.run(main())
