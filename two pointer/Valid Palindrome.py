"""
return true if the list can be a 对称 string after delete one character
e.g. abca --> delete c --> aca --> true
"""


def check_palindrome(li):
    if li == "":
        return "error"
    li = list(li)
    left = 0
    right = len(li) - 1
    while left < right:
        while left < right and li[left] == li[right]:
            left += 1
            right -= 1
        if li[left] == li[right-1]:
            del li[right]
        elif li[left+1] == li[right]:
            del li[left]
        else:
            return False
        left += 1
        right -= 1
    return True


