# sparly bot entry point

"""
Entry point for the Sparly Telegram bot.
This module configures the bot and dispatcher and starts polling.
"""

import asyncio
import os
from aiogram import Bot, Dispatcher
from aiohttp import web

from .handlers import register_handlers


async def start_bot(bot: Bot, dp: Dispatcher) -> None:
    """
    Start the Telegram bot polling in a background task.
    """
    await dp.start_polling(bot)


async def handle_root(request: web.Request) -> web.Response:
    """
    Simple HTTP handler to keep Render's web service alive.
    Returns a 200 OK response with a plain text message.
    """
    return web.Response(text="Sparly bot is running")


async def main() -> None:
    """
    Run the Telegram bot and a minimal HTTP server concurrently.
    """
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_TOKEN environment variable is missing")

    # Initialize bot and dispatcher
    bot = Bot(token=token, parse_mode="HTML")
    dp = Dispatcher()
    register_handlers(dp)

    # Start HTTP server using aiohttp
    app = web.Application()
    app.router.add_get("/", handle_root)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", "10000"))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    # Run Telegram bot polling concurrently
    bot_task = asyncio.create_task(start_bot(bot, dp))
    await bot_task


if __name__ == "__main__":
    asyncio.run(main())
