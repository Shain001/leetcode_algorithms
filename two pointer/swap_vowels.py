"""
swap the vowels alpha in a string
"""


def swap_vowels(li):
    li = list(li)
    if li is "":
        return "error"

    left = 0
    right = len(li) - 1
    vowels = ['a', 'e', 'i', 'o', 'u']
    while left < right:
        while left < right and li[left] not in vowels:
            left += 1
        while left < right and li[right] not in vowels:
            right -= 1
        li[left], li[right] = li[right], li[left]
        left += 1
        right -= 1
    li = convert_list_to_string(li)
    return li


def convert_list_to_string(li):
    converted = ""
    for i in li:
        converted += i
    return converted


print(swap_vowels('leetcode'))