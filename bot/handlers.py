"""Handlers for Sparly bot commands."""

from aiogram import Dispatcher, types
from aiogram.filters import Command

# Import helper functions from sample_data
from bot.utils.sample_data import compare_prices, get_cheapest_basket

async def start_cmd(message: types.Message) -> None:
    """Handle /start command."""
    # Send a greeting message and instructions for the user.
    await message.answer(
        "Welcome to Sparly! Use /prefs to set your preferences. "
        "Use /basket to calculate the cheapest basket or /compare <product> to compare prices."
    )

async def prefs_cmd(message: types.Message) -> None:
    """Handle /prefs command."""
    # Placeholder for preferences handling logic (language, radius, categories, etc.)
    await message.answer("Preferences command placeholder.")

async def basket_cmd(message: types.Message) -> None:
    """Handle /basket command."""
    # If the user only sends '/basket' without items, ask them to provide items.
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Please send your basket items separated by commas.")
        return
    items_raw = args[1]
    items = [item.strip() for item in items_raw.split(",") if item.strip()]
    if not items:
        await message.answer("Please provide at least one item.")
        return
    totals = get_cheapest_basket(items)
    if not totals:
        await message.answer("No data found for your items.")
        return
    # Build a response listing each store and total price
    lines = [f"{store}: {total:.2f}\u20ac" for store, total in sorted(totals.items(), key=lambda x: x[1])]
    text = "Cheapest basket options:\n" + "\n".join(lines)
    await message.answer(text)

async def compare_cmd(message: types.Message) -> None:
    """Handle /compare command to compare prices for a single product."""
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Please provide a product name, e.g. /compare eggs")
        return
    product = args[1].strip()
    offers = compare_prices(product)
    if not offers:
        await message.answer(f"No price data found for {product}.")
        return
    lines = [
        f"{offer['chain']} {offer['store_name']}: {offer['price']:.2f}\u20ac"
        for offer in offers
    ]
    text = f"Price comparison for {product}:\n" + "\n".join(lines)
    await message.answer(text)

def register_handlers(dp: Dispatcher) -> None:
    """Register command handlers with the dispatcher."""
    dp.message.register(start_cmd, Command("start"))
    dp.message.register(prefs_cmd, Command("prefs"))
    dp.message.register(basket_cmd, Command("basket"))
    dp.message.register(compare_cmd, Command("compare"))
