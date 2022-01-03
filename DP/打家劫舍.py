from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    dp = len(nums) * [0]
    dp[0] = nums[0]
    dp[1] = max(nums[1], nums[0])

    for i in range(2, len(nums)):
        dp[i] = max((nums[i] + dp[i - 2], dp[i-1]))

    return dp[-1]


print(rob([2,1,1,2]))