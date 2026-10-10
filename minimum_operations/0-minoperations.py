#!/usr/bin/python3
"""Module that calculates the fewest operations to get n H characters."""


def minOperations(n):
    """Return the fewest number of operations needed to result in exactly
    n H characters in the file, using only Copy All and Paste.

    The answer equals the sum of the prime factors of n.

    Args:
        n (int): the target number of H characters.

    Returns:
        int: the minimum number of operations, or 0 if n is impossible
             to achieve (n is not an integer or n < 2).
    """
    if not isinstance(n, int) or n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
