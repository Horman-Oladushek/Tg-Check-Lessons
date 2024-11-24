from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Router
from database.repo import Id_UsersRepo

router = Router()

class StartState(StatesGroup):
    waiting_for_message = State()


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.reply("Привет! Напишите свою фамилию, чтобы в будущем получать изменение рассписания")
    await state.set_state(StartState.waiting_for_message)

@router.message(StartState.waiting_for_message)
async def name_of_user(message: Message, state: FSMContext):
    text = message.text
    await state.clear()
    Id_UsersRepo.create(message.from_user.id, text)
    print(message.from_user.id, text)
    await message.reply(f'Ваша фамилия {text} успешно сохранена для будущих уведомлений об изменении расписания!')
    await message.answer('Чтобы изменить фамилию, напишите /start')