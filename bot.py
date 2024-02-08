import asyncio

from aiogram import Bot, Dispatcher

from misc import env


async def main():
    bot = Bot(token=env.TgKeys.TOKEN)
    dp = Dispatcher()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())