import asyncio


async def coro(task):
    print("coro waiting for the task to finish")
    await task


async def main():
    task = asyncio.current_task()
    task2 = asyncio.create_task(coro(task))
    await task2


asyncio.run(main(), debug=True)
