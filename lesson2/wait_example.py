import asyncio


async def simple_task(number):
    await asyncio.sleep(1)
    print("called")
    return number


async def error_task():
    await asyncio.sleep(0.2)
    raise ValueError("This task failed.")


async def main():
    tasks = [
        asyncio.create_task(simple_task(1)),
        asyncio.create_task(error_task()),
    ]

    done, pending = await asyncio.wait(
        tasks, 
        return_when=<TODO>, 
    )

    print("The results gathered so far are:", done)
    print("The pending tasks are:", pending)


asyncio.run(main())