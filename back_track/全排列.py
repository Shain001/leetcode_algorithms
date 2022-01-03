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





"""
2021-12-2 review
"""

def permutation_review(nums):
    """
        写回溯的程序：
        （1） 由于回溯都是用递归实现， 那么首先要确定的点，即递归的入口，也即递归方程，也即大问题由什么小问题组成。
            本题中最开始没想出来的第一个原因，[1,2,3]的全排列即为1 + [2, 3]的全排列。
        （2） 其次， 回溯算法为： ”将问题分解成各个步骤，也即树状结构。 然后再每一个步骤中依次选择各个”可能“。然后下一步再从‘未选择’的可能中选择下一个可能“。
            换句话说，回溯过程就是 ”深度遍历一颗树的过程“。
            那么， 自此可引入一回溯过程中的关键， 即”状态变量“。 状态变量用于标记 ”一个可能性是否已经被使用过“。 一个使用过的可能性则不能再被包含在下面的层级中。
            而当一条路径已经遍历结束，则此时应该开始回退过程。 在回退过程中， 一个很重要的操作即为 ”还原状态变量“， 否则这个可能性将在之后的遍历中丢失。

        那么自此可以总结写回溯程序时：
        （1） 单独思考递归：
            a. 该问题由什么子问题组成 --》 递归方程
            b. 何时该剪枝， 何时又代表已经遍历至树的最后一层 （目前来看， 应该固定的想此题一样判断是否还有可用的可能性， 即 if False not in used）--> 递归终止条件
            c. 判断状态变量是什么， 进而”向下遍历“ 过程中 ”标记状态变量“， 然后再”回退“ 过程中”还原“ 状态变量。
                而所谓 ”向下遍历过程“ 及”回退“过程 再代码中的体现即为 call function itself 之前和之后。
                即， 包括 改变状态变量 在内的， 想要再向下遍历过程中实现的操作， 都写在 调用自身 之前
                而 还原状态变量在内的操作 都写在 调用自身之后。

        More:
            函数中for 循环的部分， 实际就是搭建树的过程。 而改变 used[]数组状态的过程，即意味一个给树分层的过程。 同一循环内 （即一次调用中）
            used[]状态为False的值均在树的一层中，因为调用一次back_track本身，也就是给树加了一层。

            而在输入的数据可以有重复的版本permutation_repeat_input中。唯一的区别即是增加一个剪枝的过程。
            By the way, here we can see that pruning is not necessarily written as termination conditoin.
            举例画图后不难发现， 重复的排列只来源于一种情况， 即同一level中有相同的值。
            又因为同一level的值定在同一次back_track的调用当中。
            那么我们要做的就是只保留一个相同的值，也即节点即可。
    :param nums:
    :return:
    """
    def back_track(used, path):
        if False not in used:
            result.append(path[:])
            return

        for i in range(0, len(nums)):
            if not used[i]:
                current = nums[i]
                used[i] = True
                path.append(current)
                back_track(used, path)
                used[i] = False
                path.pop()

    if len(nums) == 1:
        return nums
    result = []
    path = []
    used = [False] * len(nums)
    back_track(used, path)
    return result


def permutation_repeat_input(nums):
    def back_track(used, path):
        if False not in used:
            # if path[:] not in result:
            result.append(path[:])
            return

        for i in range(0, len(nums)):
            if not used[i]:
                current = nums[i]
                if i >= 1 and current == nums[i-1] and used[i-1]:
                    continue

                used[i] = True
                path.append(current)
                back_track(used, path)
                used[i] = False
                path.pop()

    if len(nums) == 1:
        return nums
    nums.sort()
    result = []
    path = []
    used = [False] * len(nums)
    back_track(used, path)
    return result


print(permutation_repeat_input([1, 1, 3]))


























