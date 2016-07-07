#!/bin/python3
# coding: utf-8
"""Example source file."""


def square(x):
    """Square x.

    :param x: number to square
    :type x: int
    :returns: square of x
    :rtype: int

    >>> square(5)
    25
    """
    return(x * x)


if __name__ == '__main__':
    print(square(5))
