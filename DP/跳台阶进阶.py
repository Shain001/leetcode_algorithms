"""
    每次可跳1，2，... , n 级台阶
    跳到第n级有多少种解法

    题解：
    若每次可跳1，2， 则： f(n) = f(n-1) + f(n-2)
    若每次可跳1，2，3级， 则 f(n) = f(n-1) + f(n-2) + f(n-3)
    ...
    每次可跳1，2，3，..., n级， 则 f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f（1） + 1

    另n = n-1
    f(n-1) = f(n-2) + f(n-3) + ... + f(1) + 1
    两式相减进而得到
    f(n) - f(n-1) = f(n-1) ==> f(n) = 2f(n-1)
"""


# 递归
def jump_recursive(n):
    if n == 1:
        return 1
    return 2*jump_recursive(n-1)


# dp
def jump_dp(n):
    result = [0]*n
    result[0] = 1

    for i in range(1, n):
        result[i] = 2 * result[i-1]

    return result[-1]


# loop
def jump_loop(n):
    pre = 1
    current = 0
    for i in range(1, n):
        current = 2 * pre
        pre = current

    return current





