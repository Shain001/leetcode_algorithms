"""
    2019-11-30
    在矩阵中搜索路径， 可达返回true
    矩阵中每个格子为字符， target为一字符串


    思路：
    典型的回溯算法， 而回溯算法又通常使用递归求解，所以此时问题转化为思考：
    （1） 终止条件 （此处注意： 在回溯问题中，终止条件的作用也包含剪枝）
    （2） 函数功能 => 实际也就对应是返回值
    （3） 函数方程 => 有让递归滚起来的作用，也就是更改 函数的参数值

    首先， 确定使用回溯算法后，第一反应即应为判断剪枝条件。对于此题， 剪枝条件即为 “当前格子不等于target中对应位的字符值”。
    Specifically, 回溯算法即可抽象为一颗树，对这棵树进行深度优先遍历。树的每一层则对应着一个步骤，而每一层中的每一个节点，即对应着
    一个可能选项。 那么在此题中， 树的层数 K, 即代表这 target string 中 index 为 K 的那一个字符。 所需确定的即为 当前层中是否有
    值等于 K 的节点，也即格子。

    换句话说， 函数的功能即为 “判断若当前格子被收录至路径中，是否能导向一条有效路径”。 也即， 能导向则返回true, 反之则返回false;

    其次， 确定了函数的功能后， 函数方程即为: 判断当前格子是否符合条件， 若符合，相邻的格子是否能够导向路径。 也即 result = fun(neighbor1) or fun(neighbor2) or fun(neighbor3) or fun(neighbor4)

    最后， 终止条件则应包含两种情况：
    （1） 已经遍历至target的最后一个字符且当前格子的值等于该字符， 返回True:



     (2) 判断路径不可达， 返回False：
        不可达的两个条件：
        a. 传入的坐标值超出边界： Specifically,  由于函数方程为 “result = fun(neighbor1) or fun(neighbor2) or fun(neighbor3) or fun(neighbor4) ”
        即，只要当前格子的值符合条件，则传入相邻格子的坐标值， 而相邻格子的坐标值再传入时并未加以判断， 所以若坐标值超出边界， 则代表路径不可达， 因为已经
        没有相邻格子可继续提供接下来的路径

        b. 当前格子值不等于target[k]: 若值不相等，则直接剪枝

    注意：
    虽然回溯算法是指“依次判断当前节点的一个可能，不可行则回退然后继续进行下一个节点的尝试”， 但此题中实际是 “同时尝试所有的可能”==> result = .. or .. or...
    也即， 此题的解法"实际没有回退的这一步"。此即为什么解体时会纠结 “如何实现回退到上一节点然后尝试下一节点”, 进而导致确定不出返回值和函数什么时候返回True。

    总之注意体会 返回True 的终止条件 以及 对于超出边界的判断方法；
    关于超出边界， 在”当前节点“判断“下一节点是否可以是路径时”， 当前节点并未考虑下一节点是不是超出边界。
    对于是否超出边界的判断， 被转移到了 “当前节点”。




"""
from typing import List


def has_path(matrix: List, target):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if back_track(i, j, 0, target, matrix):
                return True

    return False


def back_track(i, j, k, target, matrix):
    if not 0 <= i <= len(matrix)-1 or not 0 <= j <= len(matrix[0])-1:
        return False

    if matrix[i][j] != target[k]:
        return False

    if k == len(target)-1 and matrix[i][j] == target[k]:
        return True

    # 目的在于避免重复的格子被录入路径之中
    # 原理在于， 只要一个坐标被传入该function中，只有两种情况： 要么该坐标的值等于target[k], 要么不等与
    # 而如果不等于的话， 在第一个if中就被剪枝了
    # 所以只要代码跑到这里， 那么当前格子必然是符合条件的， 也就是会继续向下搜寻的
    # 这意味着： 1. 当前格子值被置空后，可用target中对应index的值恢复
    # 2. 会继续向下搜寻，也就是指当前格子已经被收录于result中，则该格子不可再次被收录，所以应滞空避免重复，因为滞空后当该格子的坐标
    # 再次被传入时， 在第一个if处会被剪枝
    matrix[i][j] = ""

    result = back_track(i+1, j, k+1, target, matrix) or back_track(i-1, j, k+1, target, matrix) or \
        back_track(i, j+1, k+1, target, matrix) or back_track(i, j-1, k+1, target, matrix)

    # 探索路径结束后恢复格子值， 否则后续遍历无法进行
    matrix[i][j] = target[k]

    return result



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

word = "ABCCED"

print(has_path(board, word))