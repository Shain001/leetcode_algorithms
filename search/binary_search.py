"""
    binary search implementation;
    @:input: sorted list
    @:return: number of target
"""


def binary_search(nums, target):
    """
            :type nums: List[int]
            :type target: int
            :rtype: int
    """
    left, right = 0, len(num) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if target == nums[pivot]:
            return pivot
        elif target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return left


num = [1, 2, 3, 5, 9]
print(binary_search(num,10))
