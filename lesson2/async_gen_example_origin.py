from pprint import pprint
import asyncio
import time

pages = {
    "Alice": 1,
    "Bob": 2,
    "Charlie": 3,
}


async def fetch_tweets(username, next=None):
    await asyncio.sleep(0.5)
    global pages
    pages[username] -= 1
    return {
        "data": [{"text": "Hello, Twitter!", "author": username}],
        "next": str(time.time()) if pages[username] > 0 else None,
    }


async def fetch_all_pages(username):
    data = []
    resp = await fetch_tweets(username)
    data.extend(resp["data"])
    while resp["next"]:
        resp = await fetch_tweets(username, resp["next"])
        data.extend(resp["data"])
    return data


async def fetch_from_users():
    users = ["Alice", "Bob", "Charlie"]

    tasks = []
    for user in users:
        tasks.append(asyncio.create_task(fetch_all_pages(user)))

    results = await asyncio.gather(*tasks)
    pprint(results)


asyncio.run(fetch_from_users())
