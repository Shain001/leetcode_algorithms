"""
    2021-12-1
    地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
    一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
    也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
    因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

    first time try wrong answer 2021-12-1:
        def back_track(x, y, m, n, current_steps, k, current_k):
        if not 0 <= x <= m - 1 or not 0 <= y <= n - 1:
            return current_steps - 1
        # if current_k > k:
        #     return current_steps-1
        if current_k == k:
            return current_steps

        maximum = max(back_track(x + 1, y, m, n, current_steps + 1, k, current_k + 1),
                      back_track(x, y + 1, m, n, current_steps + 1, k, current_k + 1),
                      back_track(x - 1, y, m, n, current_steps + 1, k, current_k - 1),
                      back_track(x, y - 1, m, n, current_steps + 1, k, current_k - 1))

        return maximum
"""


def get_maximum(m: int, n: int, k: int) -> int:
    def back_track(x, y, m, n, k, si, sj):
        if not 0 <= x <= m - 1 or not 0 <= y <= n - 1 or si + sj > k or (x, y) in visited:
            return 0
        # if current_k > k:
        #     return current_steps-1
        visited.add((x, y))
        maximum = 1 + back_track(x + 1, y, m, n, k, si + 1 if x != 9 else 1, sj) + \
                  back_track(x, y + 1, m, n, k, si, sj + 1 if y != 9 else 1)

        return maximum

    if k == 0:
        return 1
    if k > m + n:
        return m * n

    visited = set()

    result = back_track(0, 0, m, n, k, 0,0)
    return result


m = 7
n = 2
k = 3
print(get_maximum(m, n, k))
