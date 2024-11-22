import asyncio
import os
from aiogram import Router, Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from handlers import start_handler, file_handler



load_dotenv()
router = Router()

async def main():
    bot = Bot(token=os.environ.get("TOKEN"))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(
        start_handler.router,
        file_handler.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    print('start')
    asyncio.run(main())
