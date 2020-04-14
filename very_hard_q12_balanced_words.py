"""
We can assign a value to each character in a word,
based on their position in the alphabet (a = 1, b = 2, ... , z = 26).
A balanced word is:
one where the sum of values on the left-hand side of the word equals the sum of values on the right-hand side.
For odd length words, the middle character (balance point) is ignored.

Write a function that returns True if the word is balanced, and False if it's not.

Examples
balanced_word("zips") ➞ True
# "zips" = "zi|ps" = 26+9|16+19 = 35|35 = True

balanced_word("brake") ➞ False
# "brake" = "br|ke" = 2+18|11+5 = 20|16 = False
Notes
All words will be lowercase, and have a minimum of 2 characters.
Palindromic words will always be balanced.
"""
from string import ascii_lowercase as al


def balanced_word(word):
    return sum(map(lambda a: al.find(a), word[:len(word) // 2])) ==\
           sum(map(lambda b: al.find(b), word[len(word) // 2 + len(word) % 2:]))

