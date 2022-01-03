"""
2021-12-7
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]

"""
from typing import List

from matplotlib import collections


def levelOrder(root) -> List[int]:
    if root is None:
        return []

    result = []
    queue = collections.deque()
    queue.append(root)

    while len(queue) != 0:
        current_node = queue.popleft()
        result.append(current_node.val)
        if current_node.left is not None:
            queue.append(current_node.left)

        if current_node.right is not None:
            queue.append(current_node.right)

    return result