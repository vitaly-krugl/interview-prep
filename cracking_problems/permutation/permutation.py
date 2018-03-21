def permutations(values):
    """Create a generator that yields permutations of the given sequence
    using an accumulator

    :param values: sequence of values to permute over

    :return: generator that yields permutations of the given sequence
    """
    # NOTE `perm=values[0:0]`: we initialize it this way in order to make perm's
    # initial value of same type as values (e.g., empty string, empty list).
    # This avoids exceptions from trying to combine values of incompatible types
    # in our helper function.
    return _doPermutations(values=values, perm=values[0:0])


def _doPermutations(values, perm):
    if not values:
        yield perm
        print(perm)
    else:
        for i in range(len(values)):
            for result in _doPermutations(
                    values=values[0:i] + values[i+1:],
                    perm=perm + values[i:i+1]):
                yield result


def permNoAccumulator(values):
    """Create a generator that yields permutations of the given sequence
    without the use of an explicit accumulator arg

    :param values: sequence of values to permute over

    :return: generator that yields permutations of the given sequence
    """
    if not values:
        # Passed empty sequence
        return
    elif len(values) == 1:
        yield values
    else:
        for i in range(len(values)):
            for perm in permNoAccumulator(values=values[0:i] + values[i+1:]):
                yield values[i:i+1] + perm
