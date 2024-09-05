import asyncio


async def simple_task(number):
    await asyncio.sleep(number)
    return number


async def long_running_task():
    await asyncio.sleep(3600)


async def main():
    task = asyncio.create_task(long_running_task())
    try:
        await asyncio.wait_for(task, timeout=3)
    except asyncio.TimeoutError:
        print("The long operation timed out, but we've handled it.")
        print(f"{task=}")
    print("This statement will run regardless.")


asyncio.run(main())
