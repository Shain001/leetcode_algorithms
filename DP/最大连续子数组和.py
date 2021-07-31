"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""


def find_max_sum(li):
    if len(li) == 1:
        return li[0]
    dp = [0] * len(li)
    dp[0] = li[0]
    # dp[1] = max(li[0] + li[1], li[1])

    for i in range(1, len(li)):
        dp[i] = max(li[i], dp[i-1] + li[i])
    return max(dp)


# 此题的省略数组的过程不是使用滚动数组，原因为返回的值并非是数组中的最大一项，而是取最大
def find_v2(li):
    maximun = li[0]
    dpi = li[0]
    for i in range(1, len(li)):
        dpi = max(li[i], li[i] + dpi)
        maximun = max(dpi, maximun)
    return maximun



test = [-2,1,-3,4,-1,2,1,-5,4]
print(find_v2(test))