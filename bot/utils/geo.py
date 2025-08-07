"""Utilities for geolocation and dynamic radius calculations."""

from typing import Dict

# Base radius in kilometers
BASE_RADIUS: float = 6.0

# Specific radii for certain chains (in kilometers)
CHAIN_RADII: Dict[str, float] = {
    "Kaufland": 15.0,
    "Globus": 15.0,
    "Lidl": 6.0,
    "Aldi": 6.0,
    "Netto": 6.0,
    "Penny": 6.0,
}


def get_radius(chain: str, user_radius: float | None = None) -> float:
    """Return the dynamic radius for a given store chain.

    If the chain has a specific radius, use it; otherwise fall back to
    the user-defined radius or the base radius.
    """
    if chain in CHAIN_RADII:
        return CHAIN_RADII[chain]
    return user_radius or BASE_RADIUS


def resolve_location(plz: str | None = None, coords: tuple[float, float] | None = None) -> tuple[float, float]:
    """Placeholder function to resolve PLZ or GPS coordinates to (lat, lon).

    In production, this should query a geocoding service or database. For
    now, it simply returns the provided coordinates or raises if none are
    available.
    """
    if coords:
        return coords
    if plz:
        # TODO: Implement PLZ to coordinates lookup
        raise NotImplementedError("PLZ geocoding is not implemented yet")
    raise ValueError("Either plz or coords must be provided")
