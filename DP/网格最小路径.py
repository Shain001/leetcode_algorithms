"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

"""
import numpy as np


def min_path(arr):
    if len(arr) == 1:
        return

    dp = np.zeros((len(arr[0]),len(arr)))
    dp[0][0] = arr[0][0]
    for i in range(1, len(arr[0])):
        dp[0][i] = dp[0][i-1] + arr[0][i]
    for j in range(1, len(arr[0])):
        dp[j][0] = dp[j-1][0] + arr[j][0]

    for i in range(1, len(arr[0])):
        for j in range(1, len(arr)):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]

    return dp[-1][-1]



def advanced(grid):
    dp = [float('inf')] * (len(grid[0]) + 1)

    dp[1] = 0
    print(dp)
    for row in grid:
        for idx, num in enumerate(row):
            dp[idx + 1] = min(dp[idx], dp[idx + 1]) + num
        print(dp)

    return dp[-1]

test = [[1,3,1],[1,5,1],[4,2,1]]
advanced(test)

