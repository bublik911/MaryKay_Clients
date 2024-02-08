import asyncio

from aiogram import Bot, Dispatcher

from misc import env

from handlers import authorization


async def main():
    bot = Bot(token=env.TgKeys.TOKEN)
    dp = Dispatcher()
    dp.include_router(authorization.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())