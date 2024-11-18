import asyncio
#import logging

from aiogram import Bot, Dispatcher
from other.Hadlers import router
from conf import TOKEN1, TOKEN2

bot = Bot(token=TOKEN2)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    #logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Ex')