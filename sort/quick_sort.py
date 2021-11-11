def quick_sort_entry(li):
    return quick_sort(li, 0, len(li) - 1)


def quick_sort(li, left, right):
    if left < right:
        pivot = partition(li, left, right)
        quick_sort(li, left, pivot-1)
        quick_sort(li, pivot+1, right)
    return li


def partition(li, left, right):
    pivot = li[left]
    while left < right:
        while left < right and li[right] >= pivot:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= pivot:
            left += 1
        li[right] = li[left]

    li[left] = pivot
    return left


print(quick_sort_entry([3,1,7,6,5,9,12,18,2]))



