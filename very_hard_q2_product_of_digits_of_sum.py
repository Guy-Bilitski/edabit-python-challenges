"""
Create a function that takes numbers as arguments, adds them together,
and returns the product of digits until the answer is only 1 digit long.

Examples
sum_dig_prod(16, 28) ➞ 6

sum_dig_prod(0) ➞ 0

sum_dig_prod(1, 2, 3, 4, 5, 6) ➞ 2
Notes
The input of the function is at least one number.
"""
import functools


def sum_dig_prod(*numbers):
    numbers_sum = numbers[0]
    if len(numbers) > 1:
        numbers_sum = functools.reduce(lambda a, b: a + b, numbers)
    while numbers_sum // 10 != 0:
        numbers_sum = functools.reduce(lambda a, b: a * b, list(map(int, str(numbers_sum))))
    return numbers_sum

