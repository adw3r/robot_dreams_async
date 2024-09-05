import asyncio


class Worker:

    __results: list[int]
    __event: asyncio.Event

    def __init__(self):
        self.__event = asyncio.Event()
        self.__results = []

    async def _counter(self, num):
        for i in range(num):
            print(f"task {i} working")
            await asyncio.sleep(0.1)
            self.__results.append(i)
        self.__event.set()

    async def do_job(self, num: int):
        asyncio.create_task(self._counter(num))

    async def get_results(self):
        print("Waiting...")
        await self.__event.wait()
        return self.__results


async def main():
    worker = Worker()
    await worker.do_job(10)
    print(await worker.get_results())


asyncio.run(main())
