#!/usr/bin/python3
"""function module"""


def makeChange(coins, total):
    """function determines the minimum
    change returned for the total"""
    if total <= 0:
        return 0

    number_of_coins = 0
    coins.sort(reverse=True)
    initial_total = total
    while total > 0:
        for denomination in coins:
            num_timez_to_minus = total // denomination
            if denomination <= total:
                total -= denomination * num_timez_to_minus
                number_of_coins += num_timez_to_minus

        if total == initial_total:
            break

        initial_total = total

    if total == 0:
        return number_of_coins
    else:
        return -1
