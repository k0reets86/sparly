# Sample data and helper functions for Sparly bot demonstration.

from typing import List, Dict

# Sample discounts data: list of dictionaries representing discount offers.
SAMPLE_DISCOUNTS: List[Dict] = [
    {
        "store_id": 1,
        "chain": "Lidl",
        "name": "Lidl München",
        "lat": 48.1351,
        "lon": 11.5820,
        "product_name": "Eggs 10pcs",
        "price": 1.19,
        "price_old": 1.49,
        "valid_until": "2025-08-10",
    },
    {
        "store_id": 2,
        "chain": "REWE",
        "name": "REWE City",
        "lat": 48.1351,
        "lon": 11.5820,
        "product_name": "Eggs 10pcs",
        "price": 1.29,
        "price_old": 1.59,
        "valid_until": "2025-08-11",
    },
    {
        "store_id": 3,
        "chain": "Lidl",
        "name": "Lidl München",
        "lat": 48.1351,
        "lon": 11.5820,
        "product_name": "Milk 1L",
        "price": 0.79,
        "price_old": 0.99,
        "valid_until": "2025-08-09",
    },
    {
        "store_id": 4,
        "chain": "REWE",
        "name": "REWE City",
        "lat": 48.1351,
        "lon": 11.5820,
        "product_name": "Butter 250g",
        "price": 1.49,
        "price_old": 1.79,
        "valid_until": "2025-08-12",
    },
]


def get_discounts() -> List[Dict]:
    """Return sample discount offers."""
    return SAMPLE_DISCOUNTS


def compare_prices(product_name: str) -> List[Dict]:
    """
    Return list of offers for a given product name across stores.

    Args:
        product_name: name of the product to search for.

    Returns:
        A list of sample discounts matching the product_name (case-insensitive).
    """
    product_name_lower = product_name.lower()
    return [
        d for d in SAMPLE_DISCOUNTS
        if product_name_lower in d["product_name"].lower()
    ]


def get_cheapest_basket(items: List[str]) -> Dict[str, float]:
    """
    Compute cheapest total price for the given items across stores.

    For demonstration purposes this function sums the lowest price per item
    from the SAMPLE_DISCOUNTS dataset without considering store grouping.

    Args:
        items: list of product names.

    Returns:
        Dictionary with total price per store (chain-name) for demonstration.
    """
    # Build a mapping of product -> cheapest offer
    cheapest: Dict[str, Dict] = {}
    for d in SAMPLE_DISCOUNTS:
        key = d["product_name"].lower()
        if key not in cheapest or d["price"] < cheapest[key]["price"]:
            cheapest[key] = d

    # Sum cheapest prices
    total_per_store: Dict[str, float] = {}
    for item in items:
        item_lower = item.lower()
        # find first matching item (simplified)
        for d_key, offer in cheapest.items():
            if item_lower in d_key:
                store = offer["name"]
                total_per_store[store] = total_per_store.get(store, 0.0) + offer["price"]
                break
    return total_per_store
