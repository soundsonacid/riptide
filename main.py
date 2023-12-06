import asyncio

from solana.rpc.async_api import AsyncClient

from driftpy.drift_client import DriftClient
from driftpy.types import *

async def main():
    async with AsyncClient("https://api.devnet.solana.com") as client:
        res = await client.is_connected()
    print(res)

asyncio.run(main())