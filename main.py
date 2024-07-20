import logging
import os
import asyncio

from pyrogram import Client, idle
from pyrogram.enums import ParseMode

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger


logging.basicConfig(level=logging.INFO)


BUSCO_MSG = '''
<emoji id="5791947163126730408">🚨</emoji> <b>BUSCO</b> <emoji id="5791947163126730408">🚨</emoji>

<blockquote>cartas</blockquote>

<emoji id="5791947163126730408">🚨</emoji> </i>responda com <code>/adbusca</code> ou <code>/adbusca ac</code></i> <emoji id="5791947163126730408">🚨</emoji>
'''

BUSCO_CHATS = [
    'me'
]


app = Client(
    'you',
    int(os.getenv('API_ID')),
    os.getenv('API_HASH'),
    'Buscobot 1.0.0',
    parse_mode=ParseMode.HTML,
    no_updates=True,
    hide_password=True
)
scheduler = AsyncIOScheduler({
    'apscheduler.timezone': 'America/Sao_Paulo'
})


async def send_busco_msg():
    for chat in BUSCO_CHATS:
        await app.send_message(chat, BUSCO_MSG)
        await asyncio.sleep(3)


async def main():
    await app.start()
    for hour in range(24):
        scheduler.add_job(
            send_busco_msg,
            CronTrigger(
                hour=hour
            )
        )
    await idle()
    await app.stop()


scheduler.start()
app.run(main())
