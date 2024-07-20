import logging
import os
import asyncio
import uvloop
from dotenv import load_dotenv

from pyrogram import Client, idle
from pyrogram.enums import ParseMode

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger


uvloop.install() # https://pyrodocs.kurimuzon.ru/topics/speedups/#uvloop
if os.path.exists('.env'):
    load_dotenv('.env')
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
    'Buscobot 1.0.1',
    parse_mode=ParseMode.HTML,
    no_updates=True,
    hide_password=True
)
scheduler = AsyncIOScheduler()


async def send_busco_msg():
    for chat in BUSCO_CHATS:
        await app.send_message(chat, BUSCO_MSG)
        await asyncio.sleep(3)


async def main():
    await app.start()
    scheduler.add_job(
        send_busco_msg,
        IntervalTrigger(
            minutes=30
        )
    )
    await idle()
    await app.stop()


scheduler.start()
app.run(main())
