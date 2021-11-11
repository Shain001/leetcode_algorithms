"""
    给定一数组，其中必有一个数字的数量大于 n/2， 找该众数
    lc.169
    思路为使用摩尔投票法，即假设众数的value为1， 其余数字value皆为-1, 那么因为众数的数量一定大于n/2, 那么另所有元素
    的value 相加（1/-1）， 得到的结果一定为整数。 因为“一个众数，和一个不是众数的数 两两一组相加为0，最后剩下的肯定为正”

"""


def fink_majority(nums):
    if len(nums) <= 2:
        return False

    majority = None
    count = 0

    for num in nums:
        """
        此处理解为：
        不想同得数都两两一组消除了，剩下的数一定是众数，因为众数个数大于n/2
        或者理解为：
        因为众数数量大于n/2， 所以数组中必定有众数相邻（若总元素个数为偶数），或者众数一定在首尾（若总元素个数为单数）。
        所以， 当依据一下if 条件判断时，必定会留下众数的count > 1。 e.g. （1，2），（1，3），（1，4），1，1
        """
        if count == 0:
            majority = num
        count += (1 if num == majority else -1)

    return majority


test = [2,2,1,1,1,2,2]
print(fink_majority(test))