"""
Description:
 Fetching data from the API and processing it in the background.
"""

import asyncio
from functools import partial
import aiohttp


async def do_fetch(session: aiohttp.ClientSession, url: str):
    print(f"Fetching data from {url}")
    async with session.get(url) as response:
        return await response.json()


async def printing(data):
    print("Processing data...")
    try:
        print(f"ID: {data['id']}, Title: {data['title']}")
    except KeyError:
        print(f"Data is not in the expected format. {data=}")


async def main():
    urls = [
        f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(100)
    ]

    async with aiohttp.ClientSession() as session:
        fetcher = partial(do_fetch, session)

        async with asyncio.TaskGroup() as tg:
            fetcher_tasks = [tg.create_task(fetcher(url)) for url in urls]

        async with asyncio.TaskGroup() as tg:
            for task in fetcher_tasks:
                data = await task
                tg.create_task(printing(data))

    print("Done!")


if __name__ == "__main__":
    asyncio.run(main())
