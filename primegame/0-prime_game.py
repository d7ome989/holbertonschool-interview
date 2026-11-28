#!/usr/bin/python3
"""Prime Game"""


def is_prime(num):
    """Return True if num is prime, otherwise False"""
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def count_primes(n):
    """Return how many primes are between 1 and n"""
    count = 0
    for i in range(1, n + 1):
        if is_prime(i):
            count += 1
    return count


def isWinner(x, nums):
    """Return the name of the player who won the most rounds"""
    maria = 0
    ben = 0
    for n in nums[:x]:
        count = count_primes(n)
        if count % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    return None
