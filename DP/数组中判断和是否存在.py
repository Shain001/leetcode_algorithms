"""
    判断给定数字是否可由数组中相加得到，相加的数可有多个
"""
import numpy as np


def rec_subset(li, i, S):
    if S == 0:
        return True
    elif i == 0:
        return li[0] == S
    elif li[i] > S:
        return rec_subset(li, i-1, S)

    return rec_subset(li, i-1, S-li[i]) or rec_subset(li, i-1, S)


# 此处， 动态规划维护2维数组，相当于把所有取值全部推出了
def dp_subset(li, S):
    dp = np.zeros((len(li), S+1), dtype=bool)
    dp[:, 0] = True
    dp[0, :] = False
    dp[0, li[0]] = True
    dp[0, 0] = True
    for i in range(1, len(li)):
        for j in range(1, S+1):
            if li[i] > j:
                dp[i, j] = dp[i-1, j]
            else:
                dp[i, j] = dp[i-1, j-li[i]] or dp[i-1, j]
    r, c = dp.shape
    return dp[r-1, c-1]

test = [3, 34, 4, 12, 5, 2]
print(dp_subset(test, 32))