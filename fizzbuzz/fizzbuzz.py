# coding=utf-8
"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for
the multiples of five output “Buzz”. For numbers which are multiples of both
three and five output “FizzBuzz”.
"""

def fizzbuzz(n):
    """ Yield fizz-buzz strings for the given input

    :param n:
    """
    for i in xrange(1, n + 1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"

        if i % 5 == 0:
            s += "Buzz"

        if not s:
            s = str(i)

        yield s
