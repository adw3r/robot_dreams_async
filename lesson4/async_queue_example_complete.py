"""
- Producer: creates and puts data into the queue
- Consumer: takes data from the queue and processes it

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
    print(f"ID: {data['id']}, Title: {data['title']}")


async def data_fetcher_worker(
    fetcher,
    urls_to_fetch: asyncio.Queue[str],
    results: asyncio.Queue[dict],
):
    while True:
        url = await urls_to_fetch.get()
        result = await fetcher(url)
        await results.put(result)
        urls_to_fetch.task_done()


async def data_processor_worker(processor, tasks: asyncio.Queue[dict]):
    while True:
        data = await tasks.get()
        await processor(data)
        tasks.task_done()


async def main():
    urls = [
        f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 100)
    ]

    q_urls_to_fetch = asyncio.Queue()
    q_data_to_process = asyncio.Queue()

    # Put the urls into the queue
    for url in urls:
        await q_urls_to_fetch.put(url)

    async with aiohttp.ClientSession() as session:
        fetcher = partial(do_fetch, session)

        fetch_worker_tasks = [
            asyncio.create_task(
                data_fetcher_worker(fetcher, q_urls_to_fetch, q_data_to_process)
            )
            for _ in range(3)
        ]

        processing = [
            asyncio.create_task(
                data_processor_worker(printing, q_data_to_process)
            )
            for _ in range(5)
        ]

        print("Waiting for all tasks to complete...")
        await q_urls_to_fetch.join()
        await q_data_to_process.join()

    print("Canceling all tasks...")
    for task in [*fetch_worker_tasks, *processing]:
        task.cancel()

    print("Waiting for cancellation")
    await asyncio.gather(
        *fetch_worker_tasks, *processing, return_exceptions=True
    )

    print("All done!")


if __name__ == "__main__":
    asyncio.run(main())
