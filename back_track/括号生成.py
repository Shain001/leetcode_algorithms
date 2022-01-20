"""
2022/1/17
leetcode 22
"""


# def generate_briscket(n):
#     def back_track(l_remain, r_remain, temp_result):
#         if l_remain == 0 and r_remain == 0:
#             to_return.append(temp_result)
#             return
#
#         print(temp_result)
#
#         if l_remain <= r_remain:
#             if l_remain > 0:
#                 back_track(l_remain - 1, r_remain, temp_result + "(")
#             if r_remain > 0:
#                 back_track(l_remain, r_remain-1, temp_result + ")")
#         # else:
#         #     if l_remain > 0:
#         #         back_track(l_remain-1, r_remain, temp_result+"(")
#
#     if n == 0:
#         return ""
#
#     to_return = []
#     back_track(n, n, "")
#     return to_return



"""
2021/1/17
答案复制于力扣题解， 主要为理解目的。

首先， 该题类似回溯思路， 实际是一个深度遍历树的过程。 每当一个字符确定， 则该层确定，应向下再走一层。 
该题的思路并不复杂， 解体关键为确定何时剪枝， 或终止递归， 对应到代码中， 就是两个if条件。
剪枝的条件即 “右括号比左括号多， e.g. ()), 此时一定剪枝”
终止条件为左右括号余额均为0.

以下为重点内容：
1. 第一眼看代码不懂的点， 以及不懂的原因:
    第一眼看时， 不懂 if left > 0 以及 if right > 0处的代码块是怎么实现了正确的输出组合的。 其实就是不懂 电脑是怎么跑的这个递归， 
    或者说这个代码电脑是怎么实现的。 
    
    其实， 重点为： ”在这种代码的写法中， 每一次return 以后（注意， 这里的return 包括手写的return, 也包括电脑递归过程中的return）,
    实际上都隐式的实现了一次‘回溯’， 也即 path.pop()， 也即 abc -> ab 的过程。“
    
    这一点如果你又看到这个代码时候又忘了的话， debug以下， 看一下 cur_str的变化即可理解。
    
    当第一次进入dfs 递归函数后， 第一次进行到 dfs(cur_str + '(', left - 1, right) 时，cur_str="", left = 2， 电脑会一直递归到 cur_str = (())才返回。
    注意： ”返回以后， 代码回到了‘第一次递归调用的入口， 也即dfs(cur_str + '(', left - 1, right)’， 此时， 代码会继续从这个入口处
    往下运行， 也即运行到 dfs(.......)......) 这一行， 从而再次进入递归， 而再此进入递归时， cur_str变成了(， left 变成了1 “
    
    
    总结， 说这么多， 就记住一句话就行： ”在这种代码的写法中， 每一次return 以后（注意， 这里的return 包括手写的return, 也包括电脑递归过程中的return）,
    实际上都隐式的实现了一次‘回溯’， 也即 path.pop()， 也即 abc -> ab 的过程。“
    
2. 上述代码错误原因：
        (1) 很久没写了， 生疏了；
        （2） 没有理解到 上述结论。
        （3） 应该用 终止条件进行的工作， 你想要用if后接逻辑做， 导致 代码运行结果不符合预期。
        实际上， 上述代码主要错误在于 没有理解好递归执行过程， 事实上， 只要 把line19-21 删除， 代码就正确了， 力扣也通过了。
        
"""
def generateParenthesis(n: int):

    res = []
    cur_str = ''

    def dfs(cur_str, left, right):
        """
        :param cur_str: 从根结点到叶子结点的路径字符串
        :param left: 左括号还可以使用的个数
        :param right: 右括号还可以使用的个数
        :return:
        """
        if left == 0 and right == 0:
            res.append(cur_str)
            return
        if right < left:
            return
        if left > 0:
            dfs(cur_str + '(', left - 1, right)
        if right > 0:
            dfs(cur_str + ')', left, right - 1)

    dfs(cur_str, n, n)
    return res


print(generateParenthesis(2))