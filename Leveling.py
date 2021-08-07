#!/usr/bin/env python3
import time, asyncio, sys


from telethon import TelegramClient, events, utils

api_id = 2394927 
api_hash = '4ab4c48f456d11a2aef03310c88c0b81'
sesi_file = 'leveling'

Leveling = '/tanamguild_Peanut_907'

    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('KampungMaifamxBot', Leveling))

    @client.on(events.NewMessage(from_users='KampungMaifamxBot'))
    async def handler(event):
        if 'Kamu berhasil menanam' in event.raw_text:
            time.sleep(2)
            await event.respond('/kebunguild_panensekarang')
            return
        
        if 'Berhasil memanen' in event.raw_text:
            time.sleep(2)
            await event.respond('/tanamguild_Peanut_907') 
            return
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	