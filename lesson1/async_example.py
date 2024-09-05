import asyncio


async def say(what, when):
    await asyncio.sleep(when)
    print(what)


async def main():
    await asyncio.gather(
        say("Martin", 2),
        say("Bob", 1),
        say("Alice", 3),
    )


if __name__ == "__main__":
    asyncio.run(main())
