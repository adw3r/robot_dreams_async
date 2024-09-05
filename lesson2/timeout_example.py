# This code snippet demonstrates how to use the asyncio.timeout context manager to cancel a task after a specified period.
import asyncio


async def long_running_task():
    # Define the long running task here
    await asyncio.sleep(3600)


async def main():
    try:
        async with asyncio.timeout(10):
            await long_running_task()
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")

    print("This statement will run regardless.")


asyncio.run(main())
