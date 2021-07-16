"""
check whether an input number is the summation of two squre number
e.g.
5 is summation of 1*1 + 2*2

tips: for all integers between 0-target, check each pair's summation;
same thing with two_nums_sum.py
"""


def check_summation_squre(target):
    if target <= 0:
        return "input error"

    li = []
    for i in range(1, target):
        li.append(i)

    left = 0
    right = len(li) - 1
    result = []

    while left < right:
        if li[left]**2 + li[right]**2 == target:
            result.append((left+1, right+1))
            left += 1
            right -= 1
        elif li[left]**2 + li[right]**2 > target:
            right -= 1
        else:
            left += 1
    return result


print(check_summation_squre(100))
