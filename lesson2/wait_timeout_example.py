import asyncio


async def long_running_task():
    await asyncio.sleep(3600)


async def short_running_task():
    await asyncio.sleep(2)


async def wait_all_completed():
    return await asyncio.wait(
        [
            asyncio.create_task(long_running_task()),
            asyncio.create_task(short_running_task()),
        ],
        return_when=asyncio.ALL_COMPLETED,
        timeout=3,
    )


async def wait_for_first_completed():
    return await asyncio.wait(
        [
            asyncio.create_task(long_running_task()),
            asyncio.create_task(short_running_task()),
        ],
        return_when=asyncio.FIRST_COMPLETED,
        timeout=3,
    )


async def wait_for_excetion():
    return await asyncio.wait(
        [
            asyncio.create_task(long_running_task()),
            asyncio.create_task(short_running_task()),
        ],
        return_when=asyncio.FIRST_EXCEPTION,
        timeout=3,
    )


async def main():
    print("-" * 50)
    done, pending = await wait_all_completed()
    print("The results gathered so far are:", done)
    print("The pending tasks are:", pending)

    print("-" * 50)
    done, pending = await wait_for_first_completed()
    print("The results gathered so far are:", done)
    print("The pending tasks are:", pending)

    print("-" * 50)
    done, pending = await wait_for_excetion()
    print("The results gathered so far are:", done)
    print("The pending tasks are:", pending)
    print("-" * 50)


asyncio.run(main())
