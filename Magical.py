import asyncio
from telethon import TelegramClient

api_id =1998603
api_hash = '341eb9d72c2de53ef2e70269728d5fca'
client = TelegramClient('sesion', api_id, api_hash)
chat ='kampungmaifamxbot'

async def main():
    async with client:
        while True:
            await client.send_message(chat, '⛏⛏⛏⛏⛏')
            await asyncio.sleep(2)

client.loop.run_until_complete(main())