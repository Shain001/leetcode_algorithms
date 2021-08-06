"""
    删除有序数组重复项
"""


def delete_repeat(arr):
    slow, fast = 0, 1
    while fast < len(arr):
        if arr[slow] == arr[fast]:
            fast += 1
        else:
            arr[slow+1] = arr[fast]
            slow += 1
            fast += 1

    return arr[:slow+1], slow+1


test = [1, 1, 2, 2, 3, 4, 5, 5]
print(delete_repeat(test))