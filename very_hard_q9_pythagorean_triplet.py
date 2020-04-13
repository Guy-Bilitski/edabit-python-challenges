"""
Create a function which validates whether 3 given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.

Examples
is_triplet(3, 4, 5) ➞ True
# 3² + 4² = 25
# 5² = 25

is_triplet(13, 5, 12) ➞ True
# 5² + 12² = 169
# 13² = 169

is_triplet(1, 2, 3) ➞ False
# 1² + 2² = 5
# 3² = 9
Notes
Numbers may not be given in a sorted order.
"""
from functools import reduce


def is_triplet(a, b, c):
    return max(a, b, c) ** 2 == reduce(lambda x, y: x**2 + y**2, filter(lambda d: d != max(a, b, c), [a, b, c]))
