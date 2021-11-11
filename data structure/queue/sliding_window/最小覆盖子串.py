"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
lc 76
"""
import collections


def fun(nums, target):
    if len(target) == 1:
        return target if target in nums else ""
    if nums == target:
        return nums

    if len(nums) < len(target):
        return ""

    need = list(target)
    max_length_final = len(nums)
    window = []
    result = []
    for i in range(len(nums)):
        if len(window) == 0:
            if nums[i] not in target:
                continue
            else:
                window.append(nums[i])
                need.remove(nums[i]) #
                continue
        if len(need) != 0:
            # if len(need)==1 and need[0] in window:
            #     window.append(nums[i])
            #     if max_length_final >= len(window):
            #         max_length_final = len(window)
            #         result = window.copy()
            #         need = [window.pop(0)]
            #         while window[0] not in target:
            #             window.pop(0)
            # else:
                window.append(nums[i])
                if nums[i] in need:
                    need.remove(nums[i])
                    if len(need) == 0:
                        if max_length_final >= len(window):
                            max_length_final = len(window)
                            result = window.copy()
                        need = [window.pop(0)]
                        while window[0] not in target:
                            window.pop(0)

                while need[0] in window:
                    if max_length_final >= len(window):
                        max_length_final = len(window)
                        result = window.copy()
                        need = [window.pop(0)]
                        while window[0] not in target:
                            window.pop(0)
    return result



def minWindow(nums, target):
    need = collections.defaultdict(int)
    for c in target:
        need[c] += 1
    start, end = 0, 0
    window = []
    max_length = len(nums)+1
    for i in range(len(nums)):
        # 判断第一次遇到t字符
        if need[nums[i]] > 0:
            pass


def minWindow3(s, t):
    from collections import defaultdict
    lookup = defaultdict(int)
    for c in t:
        lookup[c] += 1
    start = 0
    end = 0
    min_len = float("inf")
    counter = len(t)
    res = ""
    while end < len(s):
        if lookup[s[end]] > 0:
            counter -= 1
        lookup[s[end]] -= 1
        end += 1
        while counter == 0:
            # 该条件确保了窗口起始指针指向目标元素的后一位，且可去除重复
            if lookup[s[start]] == 0:
                counter += 1
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
            lookup[s[start]] += 1
            start += 1
    return res


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow3(s,t))
