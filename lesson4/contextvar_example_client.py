import asyncio


async def main():
    reader, writer = await asyncio.open_connection("localhost", 12345)
    while True:
        command = input("Enter command: ")
        if command == "exit":
            break
        writer.write(f"{command}\n".encode())
        data = await reader.readline()
        print(data.decode().strip())


asyncio.run(main())
