import asyncio


async def async_print(txt, t):
    await asyncio.sleep(t)
    print(txt)
    return txt + "!!!"


async def main():
    # would not work without await
    await asyncio.gather(
        async_print("Hello", 2),
        async_print("World", 1),
    )


asyncio.run(main())
