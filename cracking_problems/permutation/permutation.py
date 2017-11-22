def permute(values):
    results = []
    _doPermutations(values=values, perm=values[0:0], results=results)
    return results

def _doPermutations(values, perm, results):
    if not values:
        results.append(perm)
        print perm
    else:
        for i in xrange(len(values)):
            _doPermutations(
                values=values[0:i] + values[i+1:],
                perm=perm + values[i:i+1],
                results=results)
