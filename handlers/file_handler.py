import time
from aiogram.types import Message
from .find_user import Find
from aiogram import Router, F
from bot import Bot

import os

router = Router()

@router.message(F.document.file_id)
async def handle_file(message: Message, bot: Bot):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_p = file.file_path
    file_path = os.path.join(os.getcwd(), 'file', 'file_1.xls')
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    print(message.from_user.id, time.strftime("%H:%M:%S %Y-%m-%d", time.localtime()))
    await bot.download_file(file_path=file_p, destination=file_path)
    lekcii = Find(file_p.split('.')[-1])
    for telegram_id, text in lekcii.items():
        await bot.send_message(chat_id=telegram_id, text=f'Пришли изменения рассписания: {text}')
