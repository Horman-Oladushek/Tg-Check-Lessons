import time
import asyncio
import os
from aiogram import Router, Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from handlers import start_handler, file_handler, botstart_handler, find_teacher_handler



load_dotenv()
router = Router()



async def main():
    bot = Bot(token=os.environ.get("TOKEN"))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(
        botstart_handler.router,
        start_handler.router,
        file_handler.router
        # find_teacher_handler.router
    )
    start = await bot.send_message(
        chat_id=os.environ.get("HORMAN_ID"),
        text=f'Бот запущен {time.strftime("%H:%M:%S %Y-%m-%d", time.localtime())}'
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    print('start', time.strftime("%H:%M:%S %Y-%m-%d", time.localtime()))
    asyncio.run(main())
