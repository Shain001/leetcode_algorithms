"""
2021-11-25


1. 前中后序便利：
    前序： 从根节点开始，从左到右

    中序： 从最左节点开始， 即从最小开始，输出即从小到大顺序

    后序： 从最低层级开始，依次向上（网上找例子）

2. 关于递归：
    解递归问题的三个关键：
    （1） 确定函数的功能
    （2） 确定终止条件
    （3） 确定递归方程
    注意点：
    不要试图想明白递归过程后求解，只需确定以上三点！
    不要想错函数的功能（即不要想的太多），比如关于树的前序遍历，function xx_recursive (见下面代码)的功能是 PRINT CURRENT NODE'S VALUE!! This is why
    previously you always could not understand how the code work. 该函数的功能仅仅是打印current node的value值，“至于打印节点的child
    的任务，是通过递归过程实现的，也就是递归方程实现的！！”

    终止条件不要写漏， 可以在整个程序写完后，代入极限条件至递归方程如斐波那契函数中 return fun(n-2)+fun(n-1)， 则可带入n=2, 看看终止条件能return否

3. 关于非递归实现前中后序遍历， see detail explain in the method commitment
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, root=None):
        self.root = Node(root)

    def add(self, value):
        if self.root.value is None:
            self.root.value = value
            return

        new_node = Node(value)
        cur_node = self.root

        # Remember this wile condition
        while cur_node.value != value:
            if cur_node.value < value:
                if cur_node.right is None:
                    cur_node.right = new_node
                    return "inserted"
                else:
                    cur_node = cur_node.right
            elif cur_node.value > value:
                if cur_node.left is None:
                    cur_node.left = new_node
                    return "inserted"
                else:
                    cur_node = cur_node.left
        return "Node Exist"

    def search(self, target):
        if self.root.value is None:
            return "Empty List"

        cur_node = self.root

        while cur_node.value != target:
            if cur_node.value > target:
                if cur_node.left is None:
                    return "Not Found"
                else:
                    cur_node = cur_node.left

            else:
                if cur_node.right is None:
                    return "Not Found"
                else:
                    cur_node = cur_node.right

        return "Found"

    def delete(self, target):
        """
        若待删除节点存在，则删除时有四种情况：
            （1） 要删除的节点只有left child, 则删除该节点后，使其first left child 链接上已删除节点的父节点
            （2） 要删除的节点只有right child, 则删除该节点后，使其first right child 链接上已删除节点的父节点
            （3） 要删除的节点Left and right 均有child, 则此时：
            （4） 左右均空，直接删除
                a. 使其左侧子树中的最大child代替其原来位置， 即直接使其left and right 指向被删除节点的left and right 即可
                   若最大child有左子树（不可能有右子树）， 则直接将左子树连接到最大child的parent的right即可
                或：
                b. 使其右侧子树中的最大child代替其原来位置， 与a同理
                解释： 只要树的结构正确，那么左侧的最大节点以及右侧的最小节不可能既有left child 又有right child

                    if you dont understand, draw a picture and you will see
            对于根节点来说，无特殊点
            对于(1) (2) 来说， 原理相同





        :param target:
        :return:
        """

        search_result = self.get_target_and_target(target)
        if search_result is False:
            return "Not Found Target"

        parent, target_node = search_result[1], search_result[0]

        is_left = True if parent.value > target else False

        # scenario (4):
        if target_node.left is None and target_node.right is None:
            if is_left:
                parent.left = None
                return "Deleted"
            parent.right = None
            return "Deleted"

        # scenario (2):
        if target_node.left is None and target_node.right is not None:
            if is_left:
                parent.left = target_node.right
                return "Deleted"
            parent.right = target_node.right
            return "Deleted"

        # scenario (1):
        if target_node.left is not None and target_node.right is None:
            if is_left:
                parent.left = target_node.left
                return "Deleted"
            parent.right = target_node.left
            return "Deleted"

        # scenario (3):
        # find the maximum in left subtree first
        temp_node = target_node
        temp_parent = target_node
        while temp_node.right is not None:
            temp_parent = temp_node
            temp_node = temp_node.right

        # 处理temp_node的坐子树
        # 此处，如果temp_node有左子树，则直接连接，没有左子树则正好将空值赋给temp_parent，所以无需if 判断
        temp_parent.right = temp_node.left

        # make temp_node's left and right point to target_node's left and right
        temp_node.left = target_node.left
        temp_node.right = target_node.right

        return "Deleted"

    def get_target_and_target(self, target):
        if self.root.value is None:
            return False

        cur_node = self.root
        parent = self.root

        while cur_node.value != target:
            if cur_node.value > target:
                if cur_node.left is None:
                    return False
                parent = cur_node
                cur_node = cur_node.left
            else:
                if cur_node.right is None:
                    return False
                parent = cur_node
                cur_node = cur_node.right

        return cur_node, parent

    def pre_order_traversal_non_recursive(self):
        """
            前序与中序遍历区别仅为print时机不同
            中序是每次pop时print
            前序是每次push时print
        :return:
        """
        if self.root.value is None:
            return "Empty Tree"

        stack = [self.root]
        cur_node = self.root
        print(cur_node.value)
        while len(stack) != 0:
            while cur_node.left is not None:
                stack.append(cur_node.left)
                cur_node = cur_node.left
                print(cur_node.value)

            cur_node = stack.pop(-1)
            while cur_node.right is None:
                if len(stack) != 0:
                    cur_node = stack.pop(-1)
                else:
                    return

            stack.append(cur_node.right)
            cur_node = cur_node.right
            print(cur_node.value)

    def in_order_traversal_non_recursive(self):
        """
            利用栈实现
            Key Point:
            （1） 所有node皆需入栈
            （2） 入栈时检查left child, 直到left child 为空时停止压栈
            （3） 出栈时检查right child, 只要有right child, 则继续压栈
            （4） 由于出栈后，又需进行压栈操作，which means 压栈代码需再次被利用。 因此需要利用改变 current_node变量的方式实现循环
            （5） 只要出栈，第一件事即打印value

            update 2021-12-19:
                看博客"算法随手-树"中的方法， 思路是一样的， 但是代码重写了，更简洁，此处不在更新（是你自己写的）。
                重写后三个遍历顺序的代码逻辑相同， 便于记忆。
        :return:
        """
        if self.root.value is None:
            return "Empty Tree"

        stack = [self.root]
        cur_node = self.root
        while len(stack) != 0:
            # start pushing until reach the most left node
            while cur_node.left is not None:
                stack.append(cur_node.left)
                cur_node = cur_node.left

            # start poping out
            cur_node = stack.pop(-1)
            # print first
            print(cur_node.value)
            # if right child is None, then continue pop the top element of the stack
            while cur_node.right is None:
                if len(stack) != 0:
                    cur_node = stack.pop(-1)
                    print(cur_node.value)
                # if stack is empty, then finish
                else:
                    return 

            # when the program reach here, it means that:
            # a. stack is not empty yet
            # b. current node has right children, therefore we need to pushing again.
            # To achieve that, we need to reuse the previous code, but during the pushing, it is left child we need to check
            # However, when the program reaches here, it means that the current_node's left child has already been in the stack once,
            # it is the right subtree children who needs to be pushed
            # therefore we push the right child first, then make the current_node be the right child, then loop works
            stack.append(cur_node.right)
            cur_node = cur_node.right

    def post_order_traversal_non_recursive(self):
        """
         2021-12-19
        :return:
        """
        cur = self.root
        stack = []
        result = []
        prev = self.root
        # 压至最左
        # 之所以加 cur is not None是为了最开始能进入循环
        # 因为stack初始为空， 不加这个条件进不来，同时也不能更改while cur is not None这个条件。
        while len(stack) != 0 or cur is not None:
            while cur is not None:
                stack.append(cur)
                cur = cur.left

            # 此处不弹出，而是检查
            cur = stack[-1]

            # 判断append到结果与否
            # 如果cur.right为空， 那么此时必然输出value，因为当程序到此处时， 已经压至最左
            # 如果cur.right不为空，但是cur.right == prev， 则代表当前节点的右侧子树已经全部输出，可以输出当前节点了。
            if cur.right is None or cur.right == prev:
                # 只要需要append结果： 则更新prev
                # 弹出stack
                # 使cur=None实现循环目的
                result.append(cur.value)
                stack.pop(-1)
                prev = cur
                cur = None
            else:
                # 如果不符合上列判断，则两种情况：
                # 当前节点的右子树还没有被输出， 则此时cur.right不为空， 会继续到第一个while压左
                # 或者当前节点的cur.right为空，即已经没有右子树， 则会略过第一个while， 继续检查输出与否
                cur = cur.right

        return result


    def pre_order_traversal_recursive(self):
        def pre_recursive(node):
            if node is None:
                return

            print(node.value)
            pre_recursive(node.left)
            pre_recursive(node.right)

        if self.root.value is None:
            print("Empty Tree")

        pre_recursive(self.root)

    def in_order_traversal_recursive(self):
        def pre_recursive(node):
            if node is None:
                return

            pre_recursive(node.left)
            print(node.value)
            pre_recursive(node.right)

        if self.root.value is None:
            print("Empty Tree")

        pre_recursive(self.root)

    def post_order_traversal_recursive(self):
        def pre_recursive(node):
            if node is None:
                return
            pre_recursive(node.left)
            pre_recursive(node.right)
            print(node.value)

        if self.root.value is None:
            print("Empty Tree")

        pre_recursive(self.root)


tree = BST()
tree.add(10)
tree.add(6)
tree.add(14)
tree.add(4)
tree.add(8)
tree.add(12)
tree.add(16)
tree.in_order_traversal_recursive()
