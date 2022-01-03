"""
    2021-11-29 review
"""


def binary_search(nums, target):
    if len(nums) == 0:
        return False

    # in case the nums is unsorted
    nums.sort()

    right = 0
    left = len(nums)-1

    while right <= left:
        mid = (right+left)//2
        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            left = mid-1
            continue

        right = mid+1
        continue

    return -1








print(binary_search([-1,0,5],-1))



