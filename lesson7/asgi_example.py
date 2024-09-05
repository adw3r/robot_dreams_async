import logging

import aiohttp

logging.basicConfig(level=logging.DEBUG)


async def app(scope, receive, send):
    if scope["type"] != "http":
        return

    await receive()

    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbin.org/delay/3") as response:
            await response.text()

    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text/html"],
            ],
        }
    )
    await send(
        {
            "type": "http.response.body",
            "body": b"<h1>Hello, World!!111</h1>",
        }
    )
