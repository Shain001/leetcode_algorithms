"""
    selection sort
"""


def selection_sort(li):
    for i in range(len(li)-2):
        min_index = i
        for j in range(i+1, len(li)):
            if li[i] > li[j]:
                min_index = j
        li[i], li[min_index] = li[min_index], li[i]

    return li


print(selection_sort([1,3,5,7,62,1,4,5]))