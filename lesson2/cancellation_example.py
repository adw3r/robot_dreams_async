# SuperFastPython.com
# example of using asyncio shield to protect a task from cancellation
import asyncio


# define a simple asynchronous
async def simple_task(number):
    # block for a moment
    await asyncio.sleep(1)
    print("called")
    # return the argument
    return number


# cancel the given task after a moment
async def cancel_task(task):
    # block for a moment
    await asyncio.sleep(0.2)
    # cancel the task
    was_cancelled = task.cancel()
    print(f"cancelled: {was_cancelled}")


# define a simple coroutine
async def main():
    # create the coroutine
    coro = simple_task(1)

    # create a task
    task = asyncio.create_task(coro)

    # created the shielded task
    shielded = task
    # shielded = asyncio.shield(task)

    # create the task to cancel the previous task
    asyncio.create_task(cancel_task(shielded))

    # handle cancellation
    try:
        # await the shielded task
        result = await shielded

        # report the result
        print(f">got: {result}")
    except asyncio.CancelledError:
        print("shielded was cancelled")

    # wait a moment
    await asyncio.sleep(1)

    # report the details of the tasks
    print(f"shielded: {shielded}")
    print(f"task: {task}")


# start
asyncio.run(main())
