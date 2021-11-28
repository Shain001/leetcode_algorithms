def binary_search_non_re(li, target):
    def binary_search(start, end, li, target):
        while start <= end:
            mid = (start+end)//2

            if start == end and li[mid] != target:
                return False

            if li[mid] < target:
                start = mid + 1
            elif li[mid] > target:
                end = mid
            elif li[mid] == target:
                return True

    return binary_search(0, len(li)-1, li, target)


#  递归方法， 不改变原数组
def binary_search_re(li, target):
    def binary_search(start, end, li, target):
        while start <= end:
            mid = (start+end)//2

            if start == end and li[mid] != target:
                return False

            if li[mid] < target:
                return binary_search(mid+1, end, li, target)
            elif li[mid] > target:
                return binary_search(start, mid, li, target)
            elif li[mid] == target:
                return True

    return binary_search(0, len(li)-1, li, target)


# 递归方法， 改变原数组
# 该方法也可改为不改变原数组， 即复制一份原数组即可
def binary_search_v3(li, target):
    if len(li) == 1:
        return li[0] == target
    if len(li) == 0:
        return False

    start = 0
    end = len(li) - 1
    mid = (start+end)//2
    if li[mid] == target:
        return True
    elif li[mid] < target:
        return binary_search_v3(li[mid+1:], target)
    elif li[mid] > target:
        return binary_search_v3(li[:mid], target)

print(binary_search_v3([1,2,3,4,5,6],8))