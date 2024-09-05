import asyncio
import enum
from asyncio import Condition


class State(enum.Enum):
    NEW = enum.auto()
    INITIALIZED = enum.auto()
    COMPLETED = enum.auto()


class StateMachine:

    def __init__(self):
        self.state = State.NEW
        self.condition = Condition()

    def _is_initialized(self):
        return self.state is State.INITIALIZED

    def _is_completed(self):
        # print("checking if completed", self.state)
        return self.state is State.COMPLETED

    async def change_state(self, new_state: State):
        async with self.condition:
            print(f"Changing state from {self.state} to {new_state}")
            self.state = new_state
            self.condition.notify_all()

    async def init(self):
        print("Initializing...")
        await asyncio.sleep(1)
        print("Initialized!")
        await self.change_state(State.INITIALIZED)

    async def do_work(self, name: str):
        async with self.condition:
            print(name, "Waiting for condition...")
            await self.condition.wait_for(self._is_initialized)
            print(name, "Condition met, doing work...")
            await asyncio.sleep(1)
            print(name, "Work finished!")
        await self.change_state(State.COMPLETED)

    async def finilize(self):
        async with self.condition:
            print("Waiting for all tasks to complete...")
            await self.condition.wait_for(self._is_completed)
            print("All tasks completed, finalizing...")
            await asyncio.sleep(1)
            print("Finalized!")


async def main():
    stm = StateMachine()

    for i in range(10):
        asyncio.create_task(stm.do_work(f"Task {i}"))

    task_fin = asyncio.create_task(stm.finilize())
    await stm.init()
    await task_fin


asyncio.run(main())
