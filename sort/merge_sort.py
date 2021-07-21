def merge_sort(li):
    if len(li) == 1:
        return li

    mid = len(li)//2
    left = li[:mid]
    right = li[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result += left
    result += right
    return result


print(merge_sort([2, 0, 1, -3,4]))

