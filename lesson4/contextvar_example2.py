import asyncio
import contextvars

client_id = contextvars.ContextVar("client_id")


async def l1():
    print("l1: Setting client_id to 1")
    client_id.set(1)
    await asyncio.sleep(1)
    print("l1: client_id is", client_id.get())


async def l2():
    print("l2: Setting client_id to 2")
    client_id.set(2)
    await asyncio.create_task(l1(), context=contextvars.copy_context())
    print("l2: client_id is", client_id.get())


asyncio.run(l2())
