"""
    input: 输入前序遍历及中序遍历的结果，构造二叉树
    未完成， 终止条件有问题

    思路：
        pre中的第一个元素即为根节点， 确定根节点后， in中根节点两侧的元素即为左右树的元素
        利用递归求解即可
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def construct_bst(pre_order_result, in_order_result):
    if len(pre_order_result) == 1 or len(in_order_result) == 1:
        return pre_order_result[0]
    if len(pre_order_result) != len(in_order_result):
        return None


    root_node = Node(pre_order_result[0])

    root_index_in_inorder = in_order_result.index(pre_order_result[0])

    left_elements_in = in_order_result[:root_index_in_inorder]
    right_elements_in = in_order_result[root_index_in_inorder+1:]

    min_index_left_in_pre = pre_order_result.index(min(left_elements_in))
    max_index_left_in_pre = pre_order_result.index(max(left_elements_in))

    min_index_right_in_pre = pre_order_result.index(min(right_elements_in))
    max_index_right_in_pre = pre_order_result.index(max(right_elements_in))

    left_elements_pre = pre_order_result[min_index_left_in_pre:max_index_left_in_pre+1]
    right_elements_pre = pre_order_result[min_index_right_in_pre:max_index_right_in_pre+1]

    root_node.right = construct_bst(right_elements_pre, right_elements_in)
    root_node.left = construct_bst(left_elements_pre, left_elements_in)

    return root_node


print(construct_bst([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6]))


