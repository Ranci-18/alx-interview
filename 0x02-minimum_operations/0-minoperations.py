#!/usr/bin/python3
"""function module for minimum number of operations"""
def minOperations(n):
    """function to perform minimum number of operations
    - copy-paste problem"""
    if n <= 1:
        return 0

    factor = 2
    operations = 0

    while factor <= n:
        if n % factor == 0:
            operations += factor
            n /= factor
        else:
            factor += 1

    return operations
