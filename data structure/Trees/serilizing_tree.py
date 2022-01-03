from bst_review import Node


def serialize(root):

    if not root:
        return [None]

    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.value)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    return result


def deserialized(data):

    if len(data) == 0:
        return

    root = Node(data[0])
    queue = [root]
    data_inx = 1
    while queue:
        node = queue.pop(0)
        node.left = Node(data[data_inx])
        data_inx += 1
        node.right = Node(data[data_inx])
        data_inx += 1
        queue.append(node.left)
        queue.append(node.right)

    return root









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

print(serialize(root))