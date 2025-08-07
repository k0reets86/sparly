"""Handlers for Sparly bot commands."""

from aiogram import Dispatcher, types
from aiogram.filters import Command


async def start_cmd(message: types.Message) -> None:
    """Handle /start command."""
    await message.answer("Welcome to Sparly! Use /prefs to set your preferences.")


async def prefs_cmd(message: types.Message) -> None:
    """Handle /prefs command."""
    await message.answer("Preferences command placeholder.")


async def basket_cmd(message: types.Message) -> None:
    """Handle /basket command."""
    await message.answer(
        "Please send your basket items separated by commas."
    )


def register_handlers(dp: Dispatcher) -> None:
    """Register command handlers with the dispatcher."""
    dp.message.register(start_cmd, Command("start"))
    dp.message.register(prefs_cmd, Command("prefs"))
    dp.message.register(basket_cmd, Command("basket"))
