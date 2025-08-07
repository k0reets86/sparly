"""Utility functions for managing user trial periods using Redis.

This module provides helper functions to enforce a one-time trial period
for each Telegram user and device. The trial is limited to a specified
number of days (default 7).
"""
from __future__ import annotations

from datetime import timedelta
from typing import Optional

import redis

DEFAULT_TRIAL_DAYS = 7


def has_trial(user_id: int, device_hash: str, r: redis.Redis, *, days: int = DEFAULT_TRIAL_DAYS) -> bool:
    """Check whether a user or device is eligible for a trial period.

    Args:
        user_id: The Telegram user ID.
        device_hash: A hashed identifier for the user's device.
        r: A Redis client instance.
        days: Number of days the trial should last. Defaults to 7.

    Returns:
        True if the user and device do not already have a trial and the trial keys
        were successfully set. False if a trial already exists.
    """
    user_key = f"trial:{user_id}"
    device_key = f"trial:{device_hash}"
    # If either key exists, the trial has already been used
    if r.exists(user_key) or r.exists(device_key):
        return False

    ttl_seconds = days * 24 * 60 * 60
    # Set both keys with expiration
    r.set(user_key, 1, ex=ttl_seconds)
    r.set(device_key, 1, ex=ttl_seconds)
    return True
