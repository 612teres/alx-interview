#!/usr/bin/python3
"""
Prime Game
"""

def sieve_of_eratosthenes(max_n):
    """
    Precomputes primes up to max_n using the Sieve of Eratosthenes.
    """
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False

    return is_prime

def count_primes_upto_n(n, prime_lookup):
    """
    Counts the number of primes up to n using a precomputed lookup table.
    """
    return sum(prime_lookup[:n + 1])

def isWinner(x, nums):
    """
    Determines the winner of the game across x rounds.

    Args:
        x (int): Number of rounds.
        nums (list of int): List of n values for each round.

    Returns:
        str: Name of the player who won the most rounds ("Maria" or "Ben"), or None if tied.
    """
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    prime_lookup = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_upto_n(n, prime_lookup)

        # Maria wins if prime_count is odd, Ben wins if even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    x = 3
    nums = [4, 5, 1]
    print(isWinner(x, nums))
