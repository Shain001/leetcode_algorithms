"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案

"""


def two_sum(li, target):
    hash_table = dict()
    for i in range(len(li)):
        if target - li[i] in hash_table.keys():
            return i, hash_table[target - li[i]]
        hash_table[li[i]] = i

    return False


test = [3, 3]
target = 6
print(two_sum(test, target))
