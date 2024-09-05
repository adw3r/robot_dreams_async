import time
import asyncio


async def blocking(t):
    print(f"Start blocking for {t} seconds")
    time.sleep(t)
    print(f"Blocking done for {t} seconds")
    print(f"Non-blocking for {t} seconds")
    await asyncio.sleep(t)
    print(f"Non-blocking done for {t} seconds")


async def main():
    await asyncio.gather(blocking(3), blocking(2), blocking(1))


if __name__ == "__main__":
    asyncio.run(main())
