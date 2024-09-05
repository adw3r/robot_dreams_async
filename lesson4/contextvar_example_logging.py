import asyncio
import logging
import contextvars
from contextvars import ContextVar
import time

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

client_id = ContextVar("client_id")
client_id.set("unknown")

task_name = ContextVar("task_name")
task_name.set("unknown")


def log_task(msg, data):
    logger.info(
        "Client ID: %s, Task Name: %s, %s, Data: %s",
        client_id.get(),
        task_name.get(),
        msg,
        data,
    )


async def subtask(data):
    task_name.set(asyncio.current_task().get_name())
    log_task("Started", data)
    await asyncio.sleep(1)
    log_task("Completed", data)


async def handle_client(
    reader: asyncio.StreamReader, writer: asyncio.StreamWriter
):
    client_id.set(writer.get_extra_info("socket").getpeername())
    logger.info("Client connected %s", client_id.get())
    await asyncio.create_task(subtask(time.time()))

    writer.close()
    await writer.wait_closed()
    logger.info("Client disconnected %s", client_id.get())


async def main():
    server = await asyncio.start_server(
        handle_client, host="localhost", port=12345
    )
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
