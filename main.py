import asyncio
import logging

from aiogram import Bot, Dispatcher

import config as c
from app.user.user_handlers import client
from app.database.models import async_main


logging.basicConfig(level = logging.INFO)
bot = Bot(token = c.api_token)
dp = Dispatcher()


async def main():
    await async_main()
    await bot.delete_webhook(drop_pending_updates = True)
    dp.include_router(client)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Stop updates/working - bot is offline")