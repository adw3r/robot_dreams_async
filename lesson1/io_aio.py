import time
import contextlib
import requests
import asyncio
import aiohttp


@contextlib.contextmanager
def perf_time(title: str):
    start = time.perf_counter()
    yield
    print(f"{title} took {time.perf_counter() - start} seconds")


async def download_site(session: requests.Session, url: str):
    async with session.get(url) as response:
        print(f"Read {len(await response.read())} from {url}")


async def download_all_sites(sites: list[str]):
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(download_site(session, url)) for url in sites
        ]
        await asyncio.gather(*tasks)


async def main():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    await download_all_sites(sites)
    print(f"Downlaoded {len(sites)} in total")


if __name__ == "__main__":
    with perf_time("Main"):
        asyncio.run(main())
