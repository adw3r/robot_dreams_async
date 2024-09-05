import asyncpg
import asyncio


async def connect_to_db():
    conn = await asyncpg.connect(
        user="postgres",
        password="postgres",
        database="app",
        host="127.0.0.1",
        port="5432",
    )
    print("Підключено до бази даних")
    await conn.close()


asyncio.run(connect_to_db())
