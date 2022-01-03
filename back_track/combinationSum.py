"""
    2021-12-2
    leetcode 39
    给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。

    candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 

    对于给定的输入，保证和为 target 的唯一组合数少于 150 个。

    initial mistake:
        def combination_sum(nums, target):
            def back_track(path):
                if sum(path) == target:
                    result.append(path[:])
                    return

                if sum(path) > target:
                    return

                for i in range(0, len(nums)):
                    path.append(nums[i])
                    back_track(path)
                    path.pop()


            if len(nums) == 0:
                return []

            result = []
            path = []
            back_track(path)
            return result

    问题： 未考虑重复结果， 即 [2,3,1] 与 [1, 2, 3]是一样的

"""


def combination_sum(nums, target):
    def back_track(path, used):
        if sum(path) == target:
            result.append(path[:])
            used.append(path[0])
            return

        if sum(path) > target:
            return

        for i in range(0, len(nums)):
            if nums[i] in used:
                continue

            path.append(nums[i])
            back_track(path, used)
            path.pop()

    if len(nums) == 0:
        return []

    nums.sort()
    result = []
    path = []
    used = []
    back_track(path, used)

    return result

candidates = [2,3, 6, 7]

target = 9
print(combination_sum(candidates, target))