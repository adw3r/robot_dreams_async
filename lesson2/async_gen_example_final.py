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


class TweetsFetcher:

    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

        self.__has_more = True
        self.__next = None

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.__has_more is False:
            raise StopAsyncIteration

        resp = await self.func(*self.args, **self.kwargs)
        if not resp["data"]:
            raise StopAsyncIteration

        self.__next = resp["next"]
        self.__has_more = bool(self.__next)
        return resp


async def fetch_all_pages(username):
    # data = []
    # resp = await fetch_tweets(username)
    # data.extend(resp["data"])
    # while resp["next"]:
    #     resp = await fetch_tweets(username, resp["next"])
    #     data.extend(resp["data"])
    # return data

    data = [page async for page in TweetsFetcher(fetch_tweets, username)]
    # data = [page async for page in TweetsFetcher(fetch_media, username)]
    # data = [page async for page in TweetsFetcher(fetch_users)]
    # etc.
    return data


async def fetch_from_users():
    users = ["Alice", "Bob", "Charlie"]

    tasks = []
    for user in users:
        tasks.append(asyncio.create_task(fetch_all_pages(user)))

    results = await asyncio.gather(*tasks)
    pprint(results)


asyncio.run(fetch_from_users())
