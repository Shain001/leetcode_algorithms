"""
2021-12-6
 offer 26
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_subtree(a: Node, b: Node):
    """
    注意 check_subtree中的终止条件的写法和逻辑。
    再check_subtree中， 传入的两个参数状态一共五中：
    (1) a None b None: true
    (2) a None b not None: False
    (3) a not None b None: true
    (4) a not None b not None => equal: True, not equal: False


    :param a:  tree
    :param b:  subtree
    :return:
    """

    def check_subtree(a_root: Node, b_root: Node):

        # 能跑到b_root 是空， 则一定是subtree中的之前的节点已经相等了。所有此处为空的话则是b已经遍历完了，返回false
        # 如果这样无法理解， 那么就是 结合（1）（3） 发现，只要b是None， 不管a是不是None， 都为true
        if b_root is None:
            return True

        # 至此 b_root一定不为None， 也即b not None, a is None 的情况 --》 情况（2）
        if a_root is None:
            return False

        if a_root.value != b_root.value:
            return False

        # 至此 一定是状态(4)中的相等
        return check_subtree(a_root.right, b_root.right) and check_subtree(a_root.left, b_root.left)

    # 注意此处， 其中a is None的部分即是对于用户输入的检查，也是递归的终止条件。
    # 而 对b is None的判断则是单纯的用户输入检查
    if a is None or b is None:
        return False

    if a.value == b.value:
        if check_subtree(a, b):
            return True

    return is_subtree(a.left, b) or is_subtree(a.right, b)


a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)

b = Node(5)
b.left = Node(7)
print(is_subtree(a, b))
