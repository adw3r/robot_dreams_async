import asyncio


async def long_running_task():
    await asyncio.sleep(3600)
    return "Long running task completed."


async def short_running_task():
    await asyncio.sleep(2)
    return "Short running task completed."


async def main():
    long_running = asyncio.create_task(long_running_task())
    short_running = asyncio.create_task(short_running_task())
    try:
        for r in asyncio.as_completed(
            [
                long_running,
                short_running,
            ],
            timeout=3,
        ):
            print(await r)
    except asyncio.TimeoutError:
        print("The long operation timed out, but we've handled it.")

    print("This statement will run regardless.")
    print(f"{long_running=}")
    print(f"{short_running=}")


asyncio.run(main())
