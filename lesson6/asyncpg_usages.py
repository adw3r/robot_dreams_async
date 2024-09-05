import asyncio
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import asyncpg
import faker
from asyncpg import Connection, Pool

fake = faker.Faker()


@asynccontextmanager
async def connect_to_db() -> AsyncGenerator[Connection, None]:
    conn = await asyncpg.connect(
        user="postgres",
        password="postgres",
        database="app",
        host="127.0.0.1",
        port="5432",
    )

    try:
        yield conn
    finally:
        await conn.close()


@asynccontextmanager
async def connection_to_db_pool() -> AsyncGenerator[Pool, None]:
    async with await asyncpg.create_pool(
        user="postgres", password="postgres", database="app", host="localhost"
    ) as pool:
        yield pool


async def create_table(conn: Connection):
    await conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id serial PRIMARY KEY,
            name text,
            age int
        )
        """
    )


async def insert_data(conn: Connection):
    await conn.execute(
        """
        INSERT INTO users (name, age) VALUES ($1, $2)
        """,
        fake.name(),
        fake.random_int(18, 99),
    )


async def fetch_data(conn: Connection):
    """Return all users from the table."""
    result = await conn.fetch("SELECT * FROM users")
    return result


async def fetch_data_iter(conn: Connection):
    """Return all users from the table."""
    async for record in conn.cursor("SELECT * FROM users"):
        yield record


async def main():
    # To create connection pool
    # async with connection_to_db_pool() as pool:
    #     async with pool.acquire() as conn:

    async with connect_to_db() as conn:
        await create_table(conn)

        for _ in range(10):
            await insert_data(conn)

        for u in await fetch_data(conn):
            print(u)

        async with conn.transaction():
            async for u in fetch_data_iter(conn):
                print(dict(u))


asyncio.run(main())
