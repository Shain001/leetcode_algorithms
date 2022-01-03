"""
    offer27
    2021-12-6
    思路：
    所谓镜像， 实际就是交换每个节点的左右节点。
    那么问题就可分解为两个步骤：
    （1） 遍历整颗树
    （2） 交换子节点（如果存在）

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def get_mirror(root: Node):

    def exchange(node):
        if node is None:
            return

        get_mirror(node.left)
        get_mirror(node.right)
        node.left, node.right = node.right, node.left


    exchange(root)
    return root


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root = get_mirror(root)
print(root.value)
print(root.left.value)
print(root.right.value)
print(root.left.left)
print(root.left.right)



