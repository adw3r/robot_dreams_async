import requests
import aiohttp
import asyncio


def sync_fetch(t):
    print(f"Start blocking for {t} seconds")
    requests.get(f"https://httpbin.org/delay/{t}")
    print(f"Blocking done for {t} seconds")


async def async_feth(t):
    print(f"Start non-blocking for {t} seconds")
    async with aiohttp.ClientSession() as session:
        await session.get(f"https://httpbin.org/delay/{t}")
    print(f"Non-blocking done for {t} seconds")


async def process(t):
    await async_feth(t)
    sync_fetch(t)


async def main():
    await asyncio.gather(
        process(3),
        process(2),
        process(1),
        process(4),
    )


if __name__ == "__main__":
    asyncio.run(main())
