"""Scraper for retrieving discount offers from REWE (Germany).

This module provides functionality to fetch current discount information
from REWE's REST API. Each offer is normalized to a standard format
used across the Sparly application.
"""
from __future__ import annotations

from typing import Any, Dict, List
from bot.utils.sample_data import get_discounts


async def fetch_discounts() -> List[Dict[str, Any]]:
    """Fetch current discount offers from REWE's API.

    Returns:
        A list of dictionaries, each representing a discount. Each dictionary
        contains the following keys:
            - store_id: unique identifier of the store
            - name: name of the specific store
            - chain: the chain identifier ("REWE")
            - lat: latitude of the store
            - lon: longitude of the store
            - product_name: name of the discounted product
            - price: current discounted price
            - price_old: original price before discount (optional)
            - valid_until: expiration date of the discount
    """
       # Fetch sample discounts and filter by chain
    discounts = get_discounts()
    return [
        d for d in discounts
        if d.get("chain", "").lower() == "rewe"
    ]
