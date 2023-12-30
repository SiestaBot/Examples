import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://api.siesta.red:4444/smile") as response: # API change in 2024
            image = await response.text()
            print(image)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

>>> response: https://siesta.red/data/smile/smile4.gif # New link will be added later
