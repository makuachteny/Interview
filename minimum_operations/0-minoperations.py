#!/usr/bin/python3

"""
Minimum Operations

"""


def minOperations(n):
    """
    Calculates fewest number of operations needed
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
