# sparly bot entry point

"""
Entry point for the Sparly Telegram bot.
This module configures the bot and dispatcher and starts polling.
"""

import asyncio
import os

from aiogram import Bot, Dispatcher

from .handlers import register_handlers


async def main() -> None:
    """Run the bot."""
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_TOKEN environment variable is missing")
    bot = Bot(token=token, parse_mode="HTML")
    dp = Dispatcher()

    # Register handlers from handlers.py
    register_handlers(dp)

    # Start polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
