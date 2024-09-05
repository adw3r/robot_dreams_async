import aiohttp
import asyncio


async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch_url(session, "https://www.python.org")
        print(html)


asyncio.run(main())
