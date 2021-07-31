"""
最长回文子字符串
"""


def palindrome(li):
    if len(li) == 1:
        return li[0]
    dp = [[False for _ in range(len(li))] for _ in range(len(li))]
    for i in range(len(li)):
        dp[i][i] = True

    max_length = 0
    start = None
    for L in range(2, len(li)+1):
        for i in range(len(li)):
            j = i+L-1
            if j >= len(li):
                break

            if li[i] != li[j]:
                flag = False
            else:
                flag = True

            if L == 2:
                dp[i][j] = flag
            else:
                dp[i][j] = flag and dp[i+1][j-1]

            if dp[i][j] and L > max_length:
                max_length = L
                start = i
                end = j+1

    if start is not None:
        return li[start:end]
    return False


test = "abvc"
print(palindrome(test))