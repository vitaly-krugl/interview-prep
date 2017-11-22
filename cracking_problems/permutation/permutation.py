def permutations(values):
    """Create a generator that yields permutations of the given sequence
    using an accumulator

    :param values: sequence of values to permute over
    :return: generator that yields permutations of the given sequence
    """
    return _doPermutations(values=values, perm=values[0:0])


def _doPermutations(values, perm):
    if not values:
        yield perm
        print perm
    else:
        for i in xrange(len(values)):
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
        for i in xrange(len(values)):
            for perm in permNoAccumulator(values=values[0:i] + values[i+1:]):
                 yield values[i:i+1] + perm
