import asyncio


async def task(id, lock):
    for i in range(10):
        async with lock:
            print(f"task {id} working")
            await asyncio.sleep(0.1)


async def main():
    lock = asyncio.Lock()
    await asyncio.gather(*[task(i, lock) for i in range(2)])


asyncio.run(main())
