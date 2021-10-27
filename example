import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://api.siesta.red:4444/smile") as response:
            image = await response.text()
            print(image)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

>>> response: https://api.siesta.red/dt/smile/smile1.gif
