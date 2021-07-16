"""
    divide and conquer fibonac
    return n'th result
"""


def fibonac(n):
    return fibonac_imp(0, 1, n)


def fibonac_imp(a, b, n):
    if n == 0:
        return a
    return fibonac_imp(b, a + b, n-1)


print(fibonac(5))