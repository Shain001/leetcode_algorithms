"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是

所有负数均不是回文
"""


def is_palindrome(num):
    if num < 0:
        return False
    if num % 10 == 0:
        return False
    temp = 0
    back_up_num = num
    while num != 0:
        pop = num % 10
        num = (num - pop) / 10
        temp = temp * 10 + pop
    temp = int(temp)
    return temp == back_up_num


test = 123456543210
print(is_palindrome(test))