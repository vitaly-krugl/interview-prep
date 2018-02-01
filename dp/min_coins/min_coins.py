"""
Find the minimum number of coins required to construct a given sum from the
given set of coin denominations.
"""


from collections import defaultdict


class NotFound(Exception):
    pass


def minCoins(allowedCoins, target):
    """Find the minimum number of coins required to construct a given sum
    from the given set of coin denominations.

    :param allowedCoins: A set of allowed coin denominations; e.g., {1, 5, 10}
    :param target: Target sum
    :return: Two-tuple - (count, purse), where count is the discovered minimum
             value and purse is a dict having selected coin denominations as
             keys and counts of the corresponding coins as values.
    :raises: NotFound if it's impossible to assemble the target from the given
             coin denominations
    """

    # For a given amount as key, maps to the optimum collection of coins;
    # Once computation proceeds past a given value, a missing value implies that
    # the value could not be constructed from allowedCoins.
    # NOTE: this structure could be substantially optimized, but as-is it yields
    # simple code for demo purposes
    cache = dict()
    cache[0] = [] # 0 value is the base case, consisting of no coins

    # Compute minimum coins required from 1 to target
    for v in xrange(1, target + 1):
        for coin in allowedCoins:
            if coin > v:
                continue

            if v - coin in cache:
                if v not in cache or len(cache[v]) > len(cache[v - coin]) + 1:
                    cache[v] = cache[v - coin] + [coin]

    if target in cache:
        purse = defaultdict(int)
        for coin in cache[target]:
            purse[coin] += 1
        return len(cache[target]), dict(purse)
    else:
        raise NotFound


# Driver program to test above function
coins = [9, 6, 5, 1]
target = 11
print("Minimum coins required is", minCoins(coins, target))

# This code is contributed by
# Vitaly Kruglikov