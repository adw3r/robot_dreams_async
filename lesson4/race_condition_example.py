import asyncio

counter = 0


async def increment():
    global counter
    tmp = counter
    await asyncio.sleep(0)
    tmp += 1
    counter = tmp


async def main():
    tasks = [increment() for _ in range(100)]
    await asyncio.gather(*tasks)
    print(counter)


if __name__ == "__main__":
    asyncio.run(main())
