"""
2021-12-3
最长回文字串review
"""


def maximum(string):

    length = len(string)

    if length <= 1:
        return string

    dp = [[False]*length for _ in range(length)]
    max_length = 1
    start_inx = 0
    for i in range(length):
        dp[i][i] = True

    for L in range(2, length+1):
        for start in range(0, length):
            if start + L - 1 > length - 1:
                break
            else:
                if L <= 3:
                    if string[start] == string[start+L-1]:
                        dp[start][start+L-1] = True
                        if L > max_length:
                            start_inx = start
                            max_length = L
                else:
                    if string[start] == string[start+L-1]:
                        dp[start][start+L-1] = dp[start+1][start+L-2]
                        if dp[start][start+L-1] and L > max_length:
                            start_inx = start
                            max_length = L

    return string[start_inx: start_inx + max_length]


print(maximum("babad"))