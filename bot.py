import asyncio
import os
from aiogram import Router, Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from handlers import start_handler, file_handler


print('start')
load_dotenv()
router = Router()

async def main():
    bot = Bot(token=os.environ.get("TOKEN"))
    dp = Dispatcher(storage=MemoryStorage())
    print('stage1')
    dp.include_routers(
        start_handler.router,
        file_handler.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    print('stage0')
    asyncio.run(main())
