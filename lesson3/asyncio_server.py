import asyncio


async def handle_client(
    reader: asyncio.StreamReader,
    writer: asyncio.StreamWriter,
):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info("peername")

    print(f"Received {message} from {addr}")

    print(f"Send: {message}")
    writer.write(data)
    await writer.drain()

    print("Closing the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(handle_client, "localhost", 8000)
    async with server:
        await server.serve_forever()
