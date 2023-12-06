import asyncio
from dotenv import load_dotenv
import os

from anchorpy import Wallet

from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair

from driftpy.drift_client import DriftClient

from driftpy.account_subscription_config import AccountSubscriptionConfig

async def main():
    load_dotenv()

    secret = os.getenv('PRIVATE_KEY')
    url = os.getenv('RPC_URL')

    pk_stripped = secret.strip('[]').replace(' ', '').split(',')
    pk_bytes = bytes([int(b) for b in pk_stripped])
    kp = Keypair.from_bytes(pk_bytes)
    wallet = Wallet(kp)
    connection = AsyncClient(url)
    client = DriftClient(
        connection,
        wallet,
        account_subscription=AccountSubscriptionConfig("cached"),
    )
    sig = await client.initialize_user()

    print("Initialized Liquidator Drift account: ", sig)

if __name__ == "__main__":
    asyncio.run(main())