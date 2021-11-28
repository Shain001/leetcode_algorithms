import numpy as np
"""
二维数组种搜寻指定元素， 存在返回TRUE, 不存在返回False
二维数组有序，横向递增，纵向也递增

解法：
    依次访问右上角元素，若比target大， 则可消灭一行，因为右上角为一行的结尾，所有其左边的数均比其小，同理若比target小，则可消灭一列
    若依次访问左下角元素同理
    重点在于不可从左上角或右下角访问，因为无法剔除行和列
    offer2 P65
    
    Note: python 中处理二维数组两种方式： native list 或 np array
    适用np array切片时， array[行， 列] 
    array.shape[0] 行数， shape[1] 列数
"""

# 改变原数组
def search(nums, target):
    if len(nums) == 0:
        return False

    darray = np.array(nums)
    print(darray[0, -1])
    while darray.shape[1] > 0 and darray.shape[0] > 0:
        if darray[0, -1] == target:
            return True
        elif darray[0, -1] > target:
            darray = darray[:, :-1]
        else:
            darray = darray[1:, :]

    return False


print(search([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4))
