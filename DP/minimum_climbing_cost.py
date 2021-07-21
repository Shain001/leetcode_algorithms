"""
    花费最小爬楼梯
"""


def climbing_with_cost(costs):
    if len(costs) <= 2:
        return 0
    dp = [0] * (len(costs) + 1)
    for i in range(2, len(costs) + 1):
        dp[i] = min(costs[i-1]+dp[i-1], costs[i-2]+dp[i-2])
    return dp[-1]


def v2(costs):
    if len(costs) <= 2:
        return 0
    result = min(costs[0], costs[1])
    i1 = 0
    i2 = 0
    for i in range(2, len(costs) + 1):
        result = min(i1 + costs[i-1], i2 + costs[i-2])
        i2 = i1
        i1 = result
    return result

test = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(v2(test))