#!/usr/bin/python3
"""Prime Game"""


def count_primes_up_to(limit):
    """Return a list where index n holds the number of primes from 1 to n"""
    # At first, assume every number is prime (nothing is crossed out)
    is_prime = [True] * (limit + 1)
    # counts[n] will store how many primes there are from 1 to n
    counts = [0] * (limit + 1)
    total = 0

    # Start from 2 because 0 and 1 are not prime
    for num in range(2, limit + 1):
        if is_prime[num]:
            total += 1
            # Cross out the multiples of this prime
            # Smaller multiples were already crossed out by smaller primes
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
        # Save the number of primes found so far
        counts[num] = total

    return counts


def isWinner(x, nums):
    """Return the name of the player who won the most rounds"""
    # No rounds means there is no winner
    if x < 1 or not nums:
        return None

    # Only play x rounds
    rounds = nums[:x]
    # Count the primes once, up to the biggest n
    counts = count_primes_up_to(max(rounds))
    maria = 0
    ben = 0

    for n in rounds:
        # Each turn removes exactly one prime,
        # so an even number of primes means Ben wins the round
        if counts[n] % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Compare the scores
    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
