from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.reply("Привет! Напиши свою фамилию, чтобы в будущем получать изменения пар")
    # await message.answer_animation('https://media1.tenor.com/m/PFVIxY3nDS0AAAAC/devil-coy.gif')