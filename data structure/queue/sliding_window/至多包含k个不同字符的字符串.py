"""
给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。
s = "eceba", k = 2
lc 340
"""
import collections


def fun(nums, k):
    start, end = 0, 0
    occured = collections.defaultdict(int)
    count = 0
    result = [0, 0]
    while end < len(nums):
        if occured[nums[end]] == 0:
            if count < k:
                count += 1
                occured[nums[end]] += 1
            else:
                if end - start > result[1]-result[0]:
                    result = [start, end]
                while count == k:
                    occured[nums[start]] -= 1
                    if occured[nums[start]] == 0:
                        count -= 1
                    start += 1
                occured[nums[end]] += 1
                count += 1
        else:
            occured[nums[end]] += 1
            if count == k:
                while end + 1 < len(nums) and nums[end+1] == nums[end]:
                    end += 1
                if nums[-1] == nums[end]:
                    end += 1
                if end - start > result[1]-result[0]:
                    result = [start, end]
        end += 1

    return result[1]-result[0]

s = "execc"
k = 2
print(fun(s,k))