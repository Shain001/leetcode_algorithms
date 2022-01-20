"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

"""
from math import ceil


def z_change(target, num_of_row):
    if target == "" or num_of_row == 1:
        return target

    # num_of_column = ceil(len(target) / 4 * 2)
    per_set = num_of_row + num_of_row - 2
    col_per_set = 1 + (num_of_row - 2)
    num_of_column = int(len(target) / per_set * col_per_set) + 1
    temp_array = [["" for _ in range(num_of_column)] for _ in range(num_of_row)]

    # temp_array[0][0] = target[0]

    col = 0
    row = 0
    change_col = False
    go_down = True
    to_return = ""

    for i in range(0, len(target)):
        temp_array[row][col] = target[i]

        if change_col:
            col += 1

        if go_down:
            row += 1
        else:
            row -= 1

        if row == num_of_row - 1:
            go_down = False
            change_col = True

        if row == 0:
            go_down = True
            change_col = False

    for i in range(num_of_row):
        for j in range(num_of_column):
            to_return += temp_array[i][j]

    return to_return

print(z_change("ABCDE", 4))
