import unittest
import asyncio


async def fetch_data():
    await asyncio.sleep(1)
    return "data"


class TestAsyncFunctions(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.data = await asyncio.sleep(0.1, result="setup complete")

    async def asyncTearDown(self):
        await asyncio.sleep(0.1)

    async def test_fetch_data(self):
        result = await fetch_data()
        self.assertEqual(result, "data")


if __name__ == "__main__":
    unittest.main()
