from aiogram.types import Message
from .find_vega import Find
from aiogram import Router, F
from bot import Bot

import os

router = Router()

@router.message(F.document.file_id)
async def handle_file(message: Message, bot: Bot):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_p = file.file_path
    file_path = f"file/file_1.{file_p.split('.')[-1]}"

    file_path = os.path.join(os.getcwd(), 'file', 'file_1.xls')
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    print(message.from_user.id)
    await bot.download_file(file_path=file_p, destination=file_path)
    lekcii = Find(file_p.split('.')[-1])
    await message.reply(f'Пришли изменения рассписания: '
                        f'{lekcii}')
