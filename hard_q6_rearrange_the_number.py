"""
Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.

Examples
rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833

rearranged_difference(3320707) ➞ 7709823
# 7733200 - 23377 = 7709823

rearranged_difference(90010) ➞ 90981
# 91000 - 19 = 90981
Notes
N/A
"""


def rearranged_difference(number):
    pass
    min_number_as_list = sorted(list(map(int, str(number))))
    max_number_as_list = min_number_as_list[::-1]
    return int("".join(map(str, max_number_as_list))) - int("".join(map(str, min_number_as_list)))


