def binary_search(li, target):
    if len(li) == 0:
        return False

    mid = len(li)//2
    left = li[:mid]
    right = li[mid+1:]
    if li[mid] == target:
        return True
    elif li[mid] < target:
        return binary_search(right, target)
    else:
        return binary_search(left,target)



print(binary_search([1,2,3,4,5,6,7,8], 8))
