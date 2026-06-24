import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

import config
from handlers.rappels import boucle_rappels
from handlers import onboarding, profile, discovery, chat, settings, verification, admin, aide



async def definir_commandes(bot: Bot):
    commandes = [
        BotCommand(command="start", description="🏠 Home / main menu"),
        BotCommand(command="discover", description="🔥 Discover profiles"),
        BotCommand(command="matches", description="💞 My matches"),
        BotCommand(command="profile", description="👤 My profile"),
        BotCommand(command="filters", description="⚙️ My search filters"),
        BotCommand(command="cancel", description="❌ Cancel current action"),
        BotCommand(command="help", description="❓ Help & FAQ"),
    ]
    await bot.set_my_commands(commandes)


async def main():
    bot = Bot(token=config.TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(onboarding.router)
    dp.include_router(profile.router)
    dp.include_router(discovery.router)
    dp.include_router(chat.router)
    dp.include_router(settings.router)
    dp.include_router(verification.router)
    dp.include_router(admin.router)
    dp.include_router(aide.router)

    await definir_commandes(bot)

    print("M_Match démarre... 💘")
    # On lance la boucle de rappels en tâche de fond
    asyncio.create_task(boucle_rappels(bot))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())