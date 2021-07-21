"""
    爬楼梯， 一次1阶或2阶， 求爬到n阶有多少种可能
    advanced 爬楼梯：
        （1） max step > no of steps: 则可能性数量 = f(no of steps, no of steps (因为一共3阶，最大跨5阶，实际也就是最大跨
        3阶) )  = f(no_of_steps, no_of_steps-1) + 1
"""


def climbing(n):
    if n == 2:
        return 2
    if n == 1:
        return 1
    if n == 0:
        return 0

    return climbing(n-1) + climbing(n-2)


def climbing_dp(n):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]


def climbing_dp2(n):
    p = 0
    q = 1
    r = 1
    for i in range(n, 1, -1):
        p = q
        q = r
        r = p + q
        print(" " + str(i))
    return r


def climbing_advance(steps, max_step):
    if steps == 0 or max_step == 0:
        return 0
    elif steps == 1:
        return 1

    count = 0
    if steps >= max_step:
        for i in range(max_step, 0, -1):
            count += climbing_advance(steps-i, max_step)
        return count
    else:
        count = climbing_advance(steps, steps-1) + 1

    return count


#print(climbing_advance(15, 2))
# print(climbing(3))
# print(climbing_dp2(3))


