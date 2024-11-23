from bot import Bot as bot
import time
import os
from aiogram import Router

router = Router()

async def on_startup():
    await bot.send_message(
        chat_id=os.environ.get("HORMAN_ID"),
        text=f'Бот запущен {time.strftime("%H:%M:%S %Y-%m-%d", time.localtime())}'
    )
