#!/usr/bin/python3
"""Module for the makeChange function."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total.

    Args:
        coins: list of positive integer coin values.
        total: target amount.

    Returns:
        Fewest number of coins, 0 if total <= 0,
        or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    # remove duplicates and coins larger than total
    coins = sorted({c for c in coins if c <= total})
    if not coins:
        return -1

    inf = total + 1
    dp = [0] + [inf] * total

    for i in range(1, total + 1):
        for c in coins:
            if c > i:
                break
            if dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1

    return dp[total] if dp[total] != inf else -1
