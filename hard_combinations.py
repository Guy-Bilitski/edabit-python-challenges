"""
Create a function that takes a variable number of groups of items,
and returns the number of ways the items can be arranged,
with one item from each group. Order does not matter.

Examples:
combinations(2, 3) ➞ 6

combinations(3, 7, 4) ➞ 84

combinations(2, 3, 4, 5) ➞ 120
"""
import functools


def combinations(*numbers):
    return functools.reduce(lambda a, b: a * b, numbers)


