import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart


TOKEN = "7356110685:AAEgbHNp5BHlZsXj1HZhP3EJQIgcsdEjAXU"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Bonjour ! 👋 M_Match fonctionne.")


@dp.message()
async def echo(message: Message):
    await message.answer("Je t'ai bien entendu : " + message.text)


async def main():
    print("Le bot démarre...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())