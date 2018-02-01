"""
For submitting as missing Python implementation to GeegsforGeeks.org

A Dynamic Programming based Python program to find minimum of coins
to make change for a given V

Contributed by Vitaly Kruglikov
"""

class NotFound(Exception):
    pass


def minCoins(allowedCoins, V):
    """Find the minimum number of coins required to construct a given sum
    from the given set of coin denominations.

    :param allowedCoins: A set of allowed coin denominations; e.g., {1, 5, 10}
    :param V: Target sum
    :return: the minimum number of coins
    :raises: NotFound if it's impossible to assemble the target from the given
             coin denominations
    """

    # For a given amount as key, maps to the optimum number of coins;
    # Once computation proceeds past a given value, a missing value implies that
    # the value could not be constructed from allowedCoins.
    cache = dict()
    cache[0] = 0 # 0 value is the base case, consisting of no coins

    # Compute minimum coins required from 1 to V
    for v in xrange(1, V + 1):
        for coin in allowedCoins:
            if coin > v:
                continue

            if v - coin in cache:
                if v not in cache or cache[v - coin] + 1 < cache[v]:
                    cache[v] = cache[v - coin] + 1

    if V in cache:
        return cache[V]
    else:
        raise NotFound


# Driver program to test above function
coins = [9, 6, 5, 1]
V = 11
print("Minimum coins required is", minCoins(coins, V))

# This code is contributed by
# Vitaly Kruglikov