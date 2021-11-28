"""
找出数组中重复元素， 不修改原数组

数组长度为n+1， 数组中数字范围为 1 ~ n, 即数字范围比数组长度少1， 找出任意一个重复元素即可

解法 - 2种：
1. 使用与duplicate_element相同的方法， 唯一改进在于复制一份相同的数组； 该方法空间复杂度较高， 为O(n), 时间复杂度不变，也为O(n)

2. 直接利用哈希表， 空间复杂度O(n)

3. 利用二分查找以及该数组特性， 因为 “数字范围比数组长度少1”，
"""


# 空间复杂度O(n)的方法
def hash_duplicate(li):
    count = [0] * len(li)
    for i in range(0, len(li)):
        if count[li[i]] >= 1:
            return li[i]
        count[li[i]] += 1

    return False


# 不使用额外空间的方法
# 注意此方法仅适用于 数组长度为n， 数字范围为1 ~ n-1的情况
def binary_search_duplicate(li):
    def search(minimum, maximum, num):
        count_temp = 0
        for i in range(0, len(li)):
            if minimum <= li[i] <= maximum:
                count_temp += 1
        return count_temp

    end = len(li)-1
    start = 1

    while start <= end:
        mid = (start+end)//2
        count = search(start, mid, li)
        if start == end and count > 1:
            return start
        elif start == end and count <= 1:
            return False

        if count > (mid-start+1):
            end = mid
        else:
            start = mid + 1

print(binary_search_duplicate([6, 6, 6, 6, 6, 5, 6]))




