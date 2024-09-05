import asyncio
import pytest


@pytest.fixture
async def data():
    await asyncio.sleep(0.1)
    return "setup complete"


@pytest.mark.asyncio
async def test_fetch_data(data):
    async def fetch_data():
        await asyncio.sleep(1)
        return "data"

    result = await fetch_data()
    assert result == "data"
