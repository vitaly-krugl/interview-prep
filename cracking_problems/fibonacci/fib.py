def fib(n):
    """Compute the Nth Fibonacci number

    :param n: the value of N for computing the Nth Fibonacci number
    :return: Nth Fibonacci number
    """
    assert n >= 0

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibs(n):
    """ Create a generator that yields fibonacci numbers from 0th through the Nth.

    :param int n: the value of N
    :return: generator that yields fibonacci numbers through the Nth number
    """
    assert n >= 0

    if n >= 0:
        yield 0
    if n >=1:
        yield 1

    prevTwo = [0, 1]
    for i in xrange(2, n+1):
        num = sum(prevTwo)
        prevTwo[0] = prevTwo[1]
        prevTwo[1] = num
        yield num
