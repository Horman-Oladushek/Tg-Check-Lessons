'''
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
ДОДЕЛАТЬ В СЛУЧАЕ НУЖДЫ!!!!!!!!!
'''







from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Router
from .find_user import Find

router = Router()

class TeacherState(StatesGroup):
    waiting_for_message = State()


@router.message(Command("check"))
async def check_teacher(message: Message, state: FSMContext):
    await message.reply("Напиши фамилию преподователя, чтобы узнать изменения в его рассписании")
    await state.set_state(TeacherState.waiting_for_message)

@router.message(TeacherState.waiting_for_message)
async def timtetable_teacher(message: Message, state: FSMContext):
    surname = message.text
    print(surname)
    await state.clear()
    lekcii = Find()
    flag = False
    for telegram_id, text in lekcii.items():
        print(text)
        if surname in text:
            await message.reply(text)
            flag = False
        else:
            flag = True
    if flag:
        await message.reply("Этого преподователя еще нет в базе данных или изменений нет!")
