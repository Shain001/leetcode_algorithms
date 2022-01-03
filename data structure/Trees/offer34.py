"""
2021-12-20
"""
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# def find_path(root, target):
#     def back_track(node, path, cur_sum):
#         if node is not None and cur_sum + node.val > target:
#             return
#         if cur_sum == target and node is None:
#             result.append(path[:])
#             return
#         if node is None:
#             return
#
#         path.append(node.val)
#         back_track(node.left, path, cur_sum+node.val)
#         back_track(node.right, path, cur_sum+node.val)
#         path.pop()
#     result = []
#     back_track(root, [], 0)
#     return result

# def find_path(root, target):
#     def back_track(node, path, cur_sum):
#         if node is None:
#             return
#         if not node.left and not node.right and cur_sum + node.val == target:
#             path.append(node.val)
#             result.append(path[:])
#             path.pop()
#             return
#
#
#         path.append(node.val)
#         back_track(node.left, path, cur_sum+node.val)
#         back_track(node.right, path, cur_sum+node.val)
#         path.pop()
#
#     result = []
#     back_track(root, [], 0)
#     return result

def find_path(root, target):
    def back_track(node, path, cur_sum):
        if node is None:
            return

        path.append(node.val)
        if not node.left and not node.right and cur_sum + node.val == target:
            result.append(path[:])



        back_track(node.left, path, cur_sum+node.val)
        back_track(node.right, path, cur_sum+node.val)
        path.pop()

    result = []
    back_track(root, [], 0)
    return result

root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.left = Node(5)
root.right.right.right = Node(1)

print(find_path(root, 22))