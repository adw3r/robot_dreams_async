import asyncio
from contextvars import ContextVar

client_id = ContextVar("client_id")  # , default="unknown"
client_id.set("unknown")


def _set_client_id(new_id):
    client_id.set(new_id)
    return "OK"


async def handle_client(
    reader: asyncio.StreamReader, writer: asyncio.StreamWriter
):
    commands = {
        "get": lambda *_: client_id.get(),
        "set": lambda *a: _set_client_id(*a),
    }

    while True:
        data = await reader.readline()
        if not data:
            break
        command, *args = data.decode().strip().split()
        response = commands[command](*args)
        writer.write(f"{response}\n".encode())


async def main():
    server = await asyncio.start_server(
        handle_client, host="localhost", port=12345
    )
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
