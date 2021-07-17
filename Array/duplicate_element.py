"""
    return true if input list has duplicate elements

    @:input list contains positive integers
    @:return True if has duplicate
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