"""
Atbash Cipher
The Atbash cipher is an encryption method,
in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

Create a function that takes a string and applies the Atbash cipher to it.

Examples
atbash("apple") ➞ "zkkov"

atbash("Hello world!") ➞ "Svool dliow!"

atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
Notes
Capitalisation should be retained.
Non-alphabetic characters should not be altered.
"""
from string import ascii_uppercase as au
from string import ascii_lowercase as al


def change_terms(char):
    if char in au:
        return au[-au.find(char) - 1]
    if char in al:
        return al[-al.find(char) - 1]

    return char


def atbash(word):
    return "".join(map(change_terms, word))

