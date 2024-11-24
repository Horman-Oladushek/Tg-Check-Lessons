from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from .find_user import Find


router = Router()

@router.message(Command("check"))
async def check(message: Message):
    lekcii = Find(message.from_user.id)
    await message.answer(lekcii)