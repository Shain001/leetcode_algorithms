def check_back_order_traversal(nums):
    """
    2021-12-19
    思路：
    判断树的后序遍历， 则首先需明确其特点：
    数组最后一位必为根节点。 那么根节点之前的elements， 必为左右子树， 且左右子树连续， 即必一组都小于root的+一组都大于root的
    e.g. [5, 7, 6, 9, 11, 10, 8] --> root = 8; left = [5, 7, 6]; right = [9, 11, 10, 8]
    那么此时， 继续判断left和right是否符合条件即可。 上例中， 如果right = [9, 1, 11, 10, 8]则不符条件， 因为右子树中无小于root
    的元素

    至此， 可确定必为使用递归解决。

    递归：
        递归函数作用：
            判断当前列表是否符合后续遍历条件
        函数方程：
            left and right 则True
        函数终止条件：
            当list长度小于等于2， 则必为True；
            当右子树中出现比root小的元素， 则为false；

        此题特殊点在于终止条件不是简单的写于前面的if， 而是先找到左右子树， 再判断右子树是否符合。
        之所以说只需判断右子树， 是因为第一while中的左子树一定是符合条件的。 因为找到的元素都是小于root的。
    :param nums:
    :return:
    """
    def recursive(nums):
        if len(nums) <= 2:
            return True

        root = nums[-1]
        left_end = 0
        while left_end < len(nums) and nums[left_end] < root:
            # 此处注意， [5, 7, 6, 9, 11, 10, 8]中， 第一次遍历时实际left_end应该等于2, 但是这里是等于3的， 因为Left_end先
            # 加了1才判断不符合while条件。 所以再return中切片时， 切成[0: left_end]正好符合所需。
            left_end += 1

        for i in range(left_end, len(nums)):
            if nums[i] < root:
                return False
        # 注意and后的切片范围不要弄错，传入下一个递归中的数组不要带上当前root。
        return recursive(nums[0:left_end]) and recursive(nums[left_end:len(nums)-1])

    if len(nums) == 0:
        return True

    return recursive(nums)


print(check_back_order_traversal([5, 7, 6, 9, 11, 10, 8]))



