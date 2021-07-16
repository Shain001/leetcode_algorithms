"""
在"有序"数组中找出两个数，使它们的和为 target。
tips: since it is sorted list, therefore if the summation is larger than target, then it has to be the left hand side
number is too high, otherwise it would be the right hand side is too small.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


def two_nums_sum(li, target):
    left = 0
    right = len(li)-1
    result = []
    while left < right:
        if li[left] + li[right] == target:
            temp_result = (left+1, right+1)
            result.append(temp_result)
            left += 1
            right -= 1
        elif li[left] + li[right] > target:
            right -= 1
        elif li[left] + li[right] < target:
            left += 1
    return str(result)


print(two_nums_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
