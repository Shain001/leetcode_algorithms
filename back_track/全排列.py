"""
    全排列
"""


def permutation(nums):
    def back_track(nums, used, path, result, depth):
        if depth == size:
            result.append(path[:])
            return
        for i in range(size):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                back_track(nums, used, path, result, depth+1)
                used[i] = False
                path.pop()

    size = len(nums)
    used = [False for _ in range(size)]

    # this is the temporary result for one combination
    path = []
    # final result
    result = []
    # this is to identify which level is the program currently in
    depth = 0
    back_track(nums, used, path, result, depth)
    return result


nums = [1, 2, 3]
print(permutation(nums))

