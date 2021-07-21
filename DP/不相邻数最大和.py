"""
    找到一个数组中，不想临的数字的最大和，可选多个数字
"""


def find_max(li, i):
    if i == 0:
        return li[0]
    elif i == 1:
        return max(li[0], li[1])

    maximum = max(li[i] + find_max(li, i-2), find_max(li, i-1))
    return maximum


def find_max_dp(li):
    dp = [0] * len(li)
    dp[0] = li[0]
    dp[1] = max(li[0], li[1])
    for i in range(2, len(li)):
        dp[i] = max(li[i] + dp[i-2], dp[i-1])
    return dp[-1]


def find_max_dp_v2(li):
    dp0 = li[0]
    dp1 = max(li[0], li[1])
    for i in range(2, len(li)):
        dpi = max(dp0 + li[i], dp1)
        dp0 = dp1
        dp1 = dpi
    return dpi


test = [1, 2, 4, 1, 7, 8, 3]
print(find_max_dp_v2(test))