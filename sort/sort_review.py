"""
    2021-11-29
    review all sorting algorithms
"""
from typing import List


def bubble_sort(nums: List) -> List:
    """
    # wrong answer writen in 2021-11-29

    for i in range(len(nums)-1, 0):
        for j in range(len(nums)-1, i):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

    冒泡排序：
        冒泡排序每次交换相邻的两个元素
        每次循环结束后， 最大或最小的元素均被挪动至数组结尾，因此， “循环条件为每次上层循环结束后，下层循环的终点应右移”
        上述错误产生原因在与对第一层循环i的理解有误， i的作用是使第二曾循环j的终点至右移， 因为i每加1， 则意味着有 1 个元素已经被
        放置在正确位置， 也即数组的后i个元素已经排好序无需在比较

    """

    if len(nums) == 0:
        return nums

    for i in range(0, len(nums) - 1):

        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def bubble_sort_optimized(nums):
    """
        原版本代码对于一个已排序的数组，依旧需循环 n + n-1 + n-2 + ... 次， which is unefficient
        可加入标志为实现对于一个已排序的数组，时间复杂度为O(n)
        关于标志位：
        即记录每次内层循环中是否发生换位，如果没发生，则代表每两个数据间大小顺序均已符合条件，即数组已排好序
    :param nums:
    :return:
    """
    if len(nums) == 0:
        return nums
    for i in range(0, len(nums) - 1):
        no_swap = True
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                no_swap = False
        if no_swap is True:
            break

    return nums

def quick_sort(nums: List) -> List:
    """
    快排的关键即为pivot找位置
    pivot：
    可以选取任意元素为pivot
    pivot左侧皆比其小，右侧皆比其大

    为pivot选好位置后，即可将pivot左右两侧的数据分为两个数组（pivot无需再包括在其中）
    然后对两个sub arrays 进行同样操作即可


    注意理解quick_sort_recursive的终止条件
    e.g. [1,3,2] ==> pivot = index1 ==> left array = [1], right array = [2]
    以[1] 为例， 此时[1] 调用partition后返回的pivot index 为0，
    此时再传参至下列代码时
    quick_sort_recursive(left, pivot_index - 1, li)
    quick_sort_recursive(pivot_index + 1, right, li)
    left = 0, right = -1;
    left = 1, right = 0
    触发终止条件
    """
    def partition(left, right, li):
        pivot = li[left]
        while left < right:

            # 之所以加上left < right 的条件，是为了防止始终没找到符合条件的元素
            # 比如到了index 0 还比pivot大， 再减1 则会变-1， 访问li[-1] 便会报错
            while left < right and li[right] >= pivot:
                right -= 1
            # 至此，找到了比pivot小的元素， 所以应将其移到左侧，在第一次循环时， left指针指向的值为pivot，
            # 当使left = right时， 数组中重复了一个right指针指向的元素，丢失了pivot
            # 但是pivot的值已经保存在pivot变量中，所以最后会被还原
            li[left] = li[right]
            while left < right and li[left] <= pivot:
                left += 1
            # 而当程序运行至此，数组中重复的right值会被消除，因为此时right指针没动，还指向原本right值的位置，当进行此赋值操作时，
            # right值变成了left。 此时数组中又重复了一个left值
            li[right] = li[left]

        # 此时，left指针指向应该消除的重复的left值，并且此时left指针必定会移动到pivot应该所在的位置
        # 所以进行该赋值操作后，整个数组中元素没有重复，没有丢失，且pivot被转移到应在的位置
        li[left] = pivot
        return left

    def quick_sort_recursive(left, right, li):
        if left >= right:
            return
        pivot_index = partition(left, right, li)
        quick_sort_recursive(left, pivot_index - 1, li)
        quick_sort_recursive(pivot_index + 1, right, li)

    left = 0
    right = len(nums) - 1

    quick_sort_recursive(left, right, nums)
    return nums


def insert_sort(nums) -> List:
    """
        Overall, insertion sort virtually divide the array into two parts: sorted part and unsorted part
        It get one of elements in unsorted part every time and insert it into the right position of sorted part
        During the insertion process, we need to move the elements in sorted part to make space for the newly inserted one
        E.g. sorted part:
        index:    0, 1, 2, 3, 4
        element:  1, 3, 4, 5, 6      to be inserted: 2

        Then:
        index:    0, 1, 2, 3, 4, 5
        element:  1,  , 3, 4, 5, 6

    """
    if len(nums) <= 1:
        return nums

    # i 的左侧为已经排好序的元素， 右侧为未排序元素
    # 每当i右移1位，则取一个未排序元素并将其插入i的左侧为其排序
    # i的值从1开始
    for i in range(1, len(nums)):
        current = nums[i]
        j = i
        while current < nums[j-1] and j >= 1:
            # 已排序元素右移为新元素腾位置
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = current
    return nums


def merge_sort(nums) -> List:
    """
        归并即先将数组持续对半分，直到分解成单个元素
        再依次进行merge
        典型的分治思想
    """
    def merge(left: List, right: List):
        """
        2021-11-29
        错误代码：

        temp_result = []
        while len(n1) != 0 and len(n2) != 0:
            # 错误1.1：
            en1 = n1.pop(0)
            en2 = n2.pop(0)
            if en1 > en2:
                # 错误1.2：
                temp_result.append(en2)
                temp_result.append(en1)
            else:
                # 错误1：
                temp_result.append(en1)
                temp_result.append(en2)
        # 错误2
        temp_result.append(en1)
        temp_result.append(en2)
        return temp_result

        错1：
        根源在于，在merge时，有可能n1中的元素全部比n2中的小，即n1全部添加进了result以后n2才开始pop
        1.1 and 1.2 皆时assume n1， n2 必是轮流进一个， 即n1进一个后n2就进一个

        错2：
        此处以为添加剩余元素，不可直接append， 这样会使整个列表变成result中的一个元素，即[..., []] 而非 [...,...]

        """
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        result += left
        result += right
        return result

    def merge_sort_entry(nums):
        """
            merge_sort_entry 本身的函数功能 “仅仅为分解而已！” ， 看终止条件的设置即可理解。（写递归代码时需确定： 终止条件，函数功能，递归方程）
            merge排序的工作是merge function做的
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums

        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        return merge(merge_sort_entry(left), merge_sort_entry(right))

    if len(nums) <= 1:
        return nums

    return merge_sort_entry(nums)



print(bubble_sort_optimized([0,-2,4,2,-1]))
