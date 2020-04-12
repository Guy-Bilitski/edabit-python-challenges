"""
Write a function that takes a positive integer and calculates:
How many dots exist in a pentagonal shape around the center dot on the Nth iteration.

In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots.
On the third, there are 16 dots, and on the fourth there are 31 dots.

Return the number of dots that exist in the whole pentagon on the Nth iteration.

Examples
pentagonal(1) ➞ 1

pentagonal(2) ➞ 6

pentagonal(3) ➞ 16

pentagonal(8) ➞ 141
Notes
N/A
"""


def pentagonal(number):
    if number == 1:
        return 1

    return pentagonal(number - 1) + (number - 1) * 5
