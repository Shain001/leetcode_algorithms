"""
    insert sort
"""


def insert_sort(li):
    # from 1 to end of list, since at the beginning we regard first element in the list is sorted
    # this loop's i, means the last element in unsorted part.
    for i in range(1, len(li)):
        # this loop, is to compare the first element in the unsorted sublist and the elements in sorted list
        # keep swapping between unsorted one and elements in sorted part until the smaller element is found
        for j in range(i, 0, -1):
            if li[j-1] > li[j]:
                li[j - 1], li[j] = li[j], li[j - 1]
            else:
                break

    return li


