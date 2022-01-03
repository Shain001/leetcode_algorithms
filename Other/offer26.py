"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。
"""


class Node:
    def __init__(self, item=None):
        self.left = None
        self.right = None
        self.item = item


def is_subtree(subtree, tree):
    def check_subtree(subtree_node, tree_node):
        if subtree_node is None:
            return True
        if tree_node is None:
            return False
        if subtree_node.item != tree_node.item:
            return False

        return check_subtree(subtree_node.left, tree_node.left) and check_subtree(subtree_node.right, tree_node.right)

    result = False
    if tree is not None and subtree is not None:
        if tree.item == subtree.item:
            result = check_subtree(tree, subtree)
        if not result:
            result = is_subtree(subtree, tree.left)
        if not result:
            result = is_subtree(subtree, tree.right)


    return result


tree = Node(4)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(8)
tree.left.right = Node(9)

subtree = Node(2)


print(is_subtree(subtree, tree))
