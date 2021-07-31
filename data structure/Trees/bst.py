COUNT = [10]


def rec_print(root,space):

    if root == None:
        return

    space += COUNT[0]

    rec_print(root.right,space)

    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.item)

    rec_print(root.left, space)


class Node:
    def __init__(self,  item=None, left=None, right=None):
        self.left = left
        self.right = right
        self.item = item


class BST:
    def __init__(self):
        self.root = None

    def add(self, item):
        if self.root is None:
            self.root = Node(item)
            return
        node = Node(item)
        current = self.root
        while current.item != item:
            if current.item < item:
                if current.right is None:
                    current.right = node
                    return "add succeed"
                else:
                    current = current.right

            if current.item > item:
                if current.left is None:
                    current.left = node
                    return "add suceed"
                else:
                    current = current.left

        return "node exist"

    def search(self, item):
        if self.root is None:
            return "empty tree"

        current = self.root
        while current.item != item:
            if item > current.item:
                if current.right is None:
                    return "Not Found"
                current = current.right

            if item < current.item:
                if current.left is None:
                    return "Not Found"
                current = current.left
        return "Found"

    def delete(self, item):
        if self.root.item == item:
            self.root = None
        if self.search_target_delete(item) is None:
            return "Not Found"
        target_node, parent = self.search_target_delete(item)[0], self.search_target_delete(item)[1]
        # print(str(target_node.item) + " " + str(parent.item) + " " + str(target_node.left.item) + " " + str(target_node.right.item))
        is_left = parent.item > target_node.item
        #  scenario 1
        if target_node.left is None and target_node.right is None:
            if is_left:
                parent.left = None
                return "deleted"
            parent.right = None
            return "deleted"
        # scenario 2
        if target_node.left is not None and target_node.right is None:
            if is_left:
                parent.left = target_node.left
                return "deleted"
            parent.right = target_node.left
            return "deleted"
        if target_node.right is not None and target_node.left is None:
            if is_left:
                parent.left = target_node.right
                return "deleted"
            parent.right = target_node.right
            return "deleted"
        # scenario 3
        to_be_replaced = self.get_replaced(target_node)

        if is_left:
            parent.left = to_be_replaced
            return "deleted"
        parent.right = to_be_replaced
        return "deleted"

    def get_replaced(self, target):
        current = target.right
        parent = None
        successor = None
        while current is not None:
            parent = successor
            # 此处，current变为空时，successor记录的是current还没变空时的值，所以循环可行
            # 这也是为什么需要三个变量而非两个
            successor = current
            current = current.left

        # 如果找到的替换值就是待删除节点的有节点，则无需更改替换值的指针
        if successor is not target.right:
            # 找到的替换值必是右子树的最小值，即最左下角，但是其可能有右孩子，所以需将其右孩子给替换值的原parent，是空也无所谓
            parent.left = successor.right
            successor.right = target.right
        return successor

    def search_target_delete(self, item):
        if self.root is None:
            return None

        current = self.root
        parent = self.root
        while current is not None:
            if current.item == item:
                return current, parent
            if current.item > item:
                parent = current
                current = current.left
            if current.item < item:
                parent = current
                current = current.right
        return None

    # top to bottom
    def iterate_preorder_traversal(self, node):
        if node is None:
            return
        print(node.item)
        self.iterate_preorder_traversal(node.left)
        self.iterate_preorder_traversal(node.right)

    # from smallest to largest
    def inorder_traversal(self, node):
        if node is None:  # 中序遍历
            return
        self.inorder_traversal(node.left)
        print(node.item)
        self.inorder_traversal(node.right)

    # bottom to top
    # 最左下角开始打印左子树，左子树完后，自右下脚打印右子树，最后root
    def postorder_traversal(self, node):
        if node is None:
            return
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.value)



test = [1, 3, 5, 2, 15, 14, 6, 7, 10]
bst = BST()
for i in test:
    bst.add(i)
bst.delete(3)
bst.inorder_traversal(bst.root)









