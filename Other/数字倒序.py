"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。

"""


def reverse_num(num):
    reversed = 0
    while num != 0:
        pop = num % 10
        # python 在为负数取余时依然会返回正数，此处为矫正操作
        if x < 0 and pop > 0:
            pop -= 10
        reversed = reversed * 10 + pop
        num = (num - pop) / 10
        if reversed > 2 ** 31 or reversed < -2 ** 31:
            return False

    return reversed


x = 0
print(reverse_num(x))
