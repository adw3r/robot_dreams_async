import asyncio


async def coro2(lock):
    print("coro2 acquiring the lock", lock)
    async with lock:
        print("coro2 acquired the lock", lock)
        pass


async def coro1(lock):
    print("coro1 acquiring the lock", lock)
    async with lock:
        print("coro1 acquired the lock", lock)
        await coro2(lock)


async def main():
    lock = asyncio.Lock()
    await coro1(lock)


with asyncio.Runner(debug=True) as runner:
    loop = asyncio.get_event_loop()
    runner.run(main())
