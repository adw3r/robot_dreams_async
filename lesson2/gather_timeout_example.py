import asyncio
from unittest import result


async def long_running_task():
    await asyncio.sleep(3600)


async def short_running_task():
    await asyncio.sleep(2)


async def main():
    results = []
    try:
        async with asyncio.timeout(3):
            results = await asyncio.gather(
                long_running_task(), short_running_task()
            )
    except asyncio.TimeoutError:
        print("The long operation timed out, but we've handled it.")
        print("The results gathered so far are:", results)


asyncio.run(main())
