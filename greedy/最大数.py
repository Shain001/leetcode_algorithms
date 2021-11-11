"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
lc.179
"""
import functools

def find_max(nums):
    def cmp(a, b):
        if a + b > b + a:
            return 1
        elif a + b < b + a:
            return -1
        return 0

    # convert nums to list of strings
    nums_to_string = map(str, nums)
    nums_to_string = sorted(nums_to_string, key=functools.cmp_to_key(cmp), reverse=True)
    return ''.join(nums_to_string)


nums = [1, 4, 43, 6]

print(find_max(nums))

