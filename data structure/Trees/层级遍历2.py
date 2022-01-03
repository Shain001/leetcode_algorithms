"""
    2021-12-6
 leetcode 102
 层级遍历
 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。


    3
   / \
  9  20
 /   /  \
0   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [0, 15,7]
]

注意， 是[0, 15, 7] 而不是 [[0], [15, 7]]



思路：
    注意不可以利用”从上至下“ 的思路， 依次遍历每层中的每个node, 即按照如下错误代码的思路解题：
    该代码由你自己写于 2021-12-6， 这个代码的错误在于他的输出形式不符合要求， 即输出了上述”而不是“后面的格式

    class Solution:
        def levelOrder(self, root: TreeNode) -> List[List[int]]:
            def traversal(node: TreeNode):
                if node is None:
                    return
                temp = []

                if node.left is not None:
                    temp.append(node.left.val)

                if node.right is not None:
                    temp.append(node.right.val)

                if len(temp) != 0:
                    result.append(temp)

                traversal(node.left)
                traversal(node.right)


            if root is None:
                return []

            result = [[root.val]]
            traversal(root)

    正确定思路：
    为每个层级标号， 即维护一个变量level记录当前再那一层， 然后直接把非空的值加入result中的level项
"""


def levelOrder(self, root):
    def traversal(node, level):
        if node is None:
            return

        # 如果当前层数为第一次到达， 再result中加入一个新的空列表
        if len(result) < level + 1:
            result.append([])

        # 按照level，再result中的level项加入值
        result[level].append(node.val)
        traversal(node.left, level + 1)
        traversal(node.right, level + 1)

    result = []
    traversal(root, 0)
    return result