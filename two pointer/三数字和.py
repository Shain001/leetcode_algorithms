"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

"""


def three_sum(li):
    if len(li) < 3:
        return None

    li = sorted(li)
    if li[0] > 0:
        return None

    result = []
    for i in range(len(li)):
        if li[i] > 0:
            return result
        if li[i] == li[i-1]:
            continue
        j = i+1
        k = len(li) - 1
        while j < k:
            if li[i] + li[j] + li[k] == 0:
                result.append((li[i], li[j], li[k]))
            k -= 1
            j += 1
            if li[j] == li[j-1] or li[k] == li[k+1]:
                continue
    return str(result)


nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))