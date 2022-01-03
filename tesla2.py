def fun(nums):
    def check_neighbor(i, j):
        if i > rows-1 or j > cols-1 or i < 0 or j < 0:
            return
        if nums[i][j] != 1:
            return

        nums[i][j] = 0

        check_neighbor(i + 1, j)
        check_neighbor(i, j + 1)
        check_neighbor(i-1, j)
        check_neighbor(i, j-1)
        return


    if len(nums) == 0:
        return 0

    cols = len(nums[0])
    rows = len(nums)

    # return
    to_return = 0

    # 遍历输入
    # 遇1加1
    # 判断相邻元素， 且更改状态

    for i in range(rows):
        for j in range(cols):
            if nums[i][j] == 1:
                # to_return += 1
                # nums[i][j] = 0
                check_neighbor(i, j)
                to_return += 1
            else:
                continue

    return to_return


test = [

[1,0,0,1,1,0],

[0,0,0,1,1,0],

[1,0,0,0,0,0],

[1,1,0,1,1,0],

]

print(fun(test))