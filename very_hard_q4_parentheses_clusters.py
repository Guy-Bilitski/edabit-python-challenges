"""
Write a function that groups a string into parentheses cluster. Each cluster should be balanced.

Examples
split("()()()") ➞ ["()", "()", "()"]

split("((()))") ➞ ["((()))"]

split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]

split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]
Notes
All input strings will only contain parentheses.
Balanced: Every opening parens ( must exist with its matching closing parens ) in the same cluster.
"""


def split(parentheses):
    list_of_parentheses = []
    close_parentheses = ''
    balance = 0
    for parens in parentheses:
        if parens == '(':
            balance += 1
            close_parentheses += parens
        else:
            balance -= 1
            close_parentheses += parens

        if balance == 0:
            list_of_parentheses.append(close_parentheses)
            close_parentheses = ''

    return list_of_parentheses

