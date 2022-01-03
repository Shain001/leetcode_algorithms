"""
2021-12-07

Z字型层级遍历二叉树
"""
from typing import List

from matplotlib import collections

from bst_review import Node


def levelOrder(root: Node) -> List[List[int]]:
    if root is None:
        return []

    result = []
    stack_push_from_left = []
    stack_push_from_right = [root]
    while len(stack_push_from_left) != 0 or len(stack_push_from_right) != 0:
        temp = []
        while len(stack_push_from_right) != 0:
            node = stack_push_from_right.pop(-1)
            temp.append(node.val)
            if node.left is not None:
                stack_push_from_left.append(node.left)
            if node.right is not None:
                stack_push_from_left.append(node.right)
        if temp:
            result.append(temp)
            temp = []

        while len(stack_push_from_left) != 0:
            node = stack_push_from_left.pop(-1)
            temp.append(node.val)
            if node.right is not None:
                stack_push_from_right.append(node.right)
            if node.left is not None:
                stack_push_from_right.append(node.left)
        if temp:
            result.append(temp)

    return result
