"""Scraper for retrieving discount offers from Lidl and Lidl Plus.

This module will interact with Lidl's public endpoints and Lidl Plus JSON
feeds to collect current promotional offers. Each offer is normalized to a
consistent dictionary format used by the Sparly application.
"""
from __future__ import annotations

from typing import Any, Dict, List
from bot.utils.sample_data import get_discounts


async def fetch_discounts() -> List[Dict[str, Any]]:
    """Fetch current discount offers from Lidl and Lidl Plus.

    Returns:
        A list of dictionaries containing discount information with the keys:
            - store_id
            - name
            - chain ("Lidl")
            - lat
            - lon
            - product_name
            - price
            - price_old
            - valid_until
    """
    # TODO: Implement scraping from Lidl website and Lidl Plus API.
       # Fetch sample discounts and filter by chain
    discounts = get_discounts()
    return [
        d for d in discounts
        if d.get("chain", "").lower() == "lidl"
    ]
