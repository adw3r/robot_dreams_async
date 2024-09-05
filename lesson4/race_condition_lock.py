import asyncio

counter = 0


async def increment(lock):
    async with lock:
        global counter
        tmp = counter
        await asyncio.sleep(0)
        tmp += 1
        counter = tmp


async def main():
    lock = asyncio.Lock()  # or asyncio.Semaphore(1) or asyncio.Barrier(1)
    tasks = [increment(lock) for _ in range(100)]
    await asyncio.gather(*tasks)
    print(counter)


if __name__ == "__main__":
    asyncio.run(main())
