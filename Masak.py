#!/usr/bin/env python3
import time, asyncio, sys


from telethon import TelegramClient, events, utils, Button

api_id = 2394927 
api_hash = '4ab4c48f456d11a2aef03310c88c0b81'
sesi_file = 'casino'

Casino = '/masak_MiniBacon_220'

    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('KampungMaifamXBot', Casino))

    @client.on(events.NewMessage(from_users='KampungMaifamXBot'))
    async def handler(event):
        if 'Berhasil memasak' in event.raw_text:
            time.sleep(2)
            await event.respond('/masak_MiniBacon_220')
            return
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	
