"""
查找某数是否在数组中（有序数组）， 若不在，则插入相应位置，在则返回下标
lc. 35
"""


def binary_search(arr, target):
    length = len(arr)
    low = 0
    high = length-1

    # 注意等于号
    while low <= high:
        mid = (high - low) // 2 + low # 防止溢出
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1

    return low


nums = [1,3,5,6]
target = 7
print(binary_search(nums, target))
