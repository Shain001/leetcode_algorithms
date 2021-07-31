"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。
"""


def jump(li):
    max_current = 0
    for i in range(len(li)):
        temp = i + li[i]
        max_current = max(temp, max_current)

    if max_current > len(li)-1:
        return True

    return False


"""
给你一个非负整数数组 nums ，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

假设你总是可以到达数组的最后一个位置。
"""


def jump2(li):
    max_current, steps, end = 0, 0, 0
    for i in range(len(li)):
        max_current = max(max_current, i + li[i])
        if i == end:
            end = max_current
            steps += 1
    return steps

