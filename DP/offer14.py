"""
    2021-12-2

    注意：
    剪n段，但n并非输入的值
    同时，注意：
                if results[j]*results[i-j] > max:
                max = results[j]*results[i-j]
        曾写成：
                if j*results[i-j] > max:
                max = j*results[i-j]
        之所以写错，是因为理解错了： ”切了第一刀后，绳子分成了两半，并非只有其中一半留着不动，切出来的两条绳子均可继续分“。比如m=8，
        第一下去分成 3， 5. 这两段都可以继续切。
        这也是为什么说上曾循环代表的是第一刀有m-1中选择。

    以上为DP的思路
    此题可贪婪算法求解，进而得到一个O(1)时间复杂度的算法
    原理为（记住即可）： 当绳长大于等于5时，尽量多的分出长度等于3的绳子，那么此时： 余数可能为： 1， 2； 如果余数为1， 则将一段3分给1，得到4
                        若绳长小于等于4， 则最大乘积为4
"""


def maximum(m):
    if m <=1:
        return m
    if m == 2:
        return 1
    if m == 3:
        return 2

    results = [0] * (m+1)
    results[1] = 1
    results[2] = 2
    results[3] = 3

    for i in range(4, m+1):
        max = 0
        for j in range(1, i):
            if results[j]*results[i-j] > max:
                max = results[j]*results[i-j]
        results[i] = max

    return results[-1]



