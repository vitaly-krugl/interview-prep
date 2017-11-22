def permutations(values):
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
