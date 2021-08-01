def inorder_traversal(self, root):
    WHITE, GRAY = 0, 1
    res = []
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if node is None:
            continue
        if color == WHITE:
            stack.append((WHITE, node.right))
            stack.append((WHITE, node.left))
            stack.append((GRAY, node))
        else:
            res.append(node.val)
    return res


