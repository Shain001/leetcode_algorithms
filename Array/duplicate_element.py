"""
    return true if input list has duplicate elements

    @:input list contains positive integers
    @:return True if has duplicate
    用set即可，无需这么复杂
"""


def find_duplicate(li):
    for i in range(len(li)):
        while i != li[i]:
            # if 
            if li[i] == li[li[i]]:
                return True

            # Swap the integers, this is for sorting purpose
            li[i], li[li[i]] = li[li[i]], li[i]

    return False


nums = [1,1,2,3,4,0]
print(find_duplicate(nums))