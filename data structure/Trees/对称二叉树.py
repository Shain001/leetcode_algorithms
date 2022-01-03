from bst_review import Node
"""
    2021-12-6
    offer28

    对称二叉树。 一棵树如果与本身的镜像相同，则为对称二叉树。

    解法：
    实际上，要判断对称二叉树，新创建一个“对称前序遍历”的方法，将其结果与正常的前序遍历比较即可。

    但需包括结果中需包括空值， 例子看offer P178
"""


def is_symmetrical(root: Node):
    def recur(left, right):
        if left is None and right is not None:
            return False

        if right is None and left is not None:
            return False

        if left is None and right is None:
            return True

        if left.val != right.val:
            return False

        # 当程序运行到这， 说明两个节点的值是相等的，因为可能造成不对称的情况都已被上述终止条件拦截了
        # 那么只需继续判断两个当先节点下的子树是否对称即可
        # 而此处return的这种形式，可以经常被套用再从上至下遍历树的问题。
        return recur(left.right, right.left) and recur(left.left, right.right)

    if root is None:
        return True
    return recur(root.left, root.right)