import asyncio
import pytest


async def retrive():
    await asyncio.sleep(0.1)
    return {"data": "data"}


def process(data):
    return "processed"


async def notify(data):
    await asyncio.sleep(0)
    return "notified"


async def do_work(timeout=0.5):
    async with asyncio.timeout(timeout):
        data = await retrive()
        loop = asyncio.get_event_loop()
        out = await loop.run_in_executor(None, process, data)
        await notify(out)


@pytest.mark.asyncio
async def test_should_check_timeout_config(mocker):

    # creating a fake retrive function that takes additional 0.5 seconds to return
    async def fake_retrive():
        await asyncio.sleep(0.1)
        return await retrive()

    mocker.patch("test_pytest_timeout_example.retrive", fake_retrive)

    with pytest.raises(asyncio.TimeoutError):
        await do_work(timeout=0.5)
