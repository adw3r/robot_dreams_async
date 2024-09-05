import time
import asyncio
from asyncio import Semaphore
from aiohttp import ClientSession


async def get_url(url: str, session: ClientSession, semaphore: Semaphore):
    async with semaphore:
        start = time.perf_counter()
        try:
            async with asyncio.timeout(10):
                response = await session.get(url)
                return response.status
        except asyncio.TimeoutError:
            print(f"Timeout requesting {url}")
            end = time.perf_counter()
            print(f"Request to {url} took {end - start:.2f} seconds")


async def main():
    semaphore = Semaphore(5)
    async with ClientSession() as session:
        tasks = [
            asyncio.create_task(
                get_url("https://httpbin.org/delay/5", session, semaphore)
            )
            for _ in range(200)
        ]
        await asyncio.gather(*tasks)


asyncio.run(main())
