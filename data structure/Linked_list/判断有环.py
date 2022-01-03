"""
    判断列表是否有环
"""


from Minor_Thesis.Linked_list import *

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3


def check_circle(node):
    slow = node
    fast = node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def find_circle_entrance(node):
    """
    当快慢指针相遇，则说明有环，若无环则说明尾节点指向null，循环自动会终止，因此不会产生无限循环
    当快慢指针相遇时，创建一新指针从头节点出发， 当该新指针与慢指针相遇时所处的结点即为环的入口
    :param node:
    :return:
    """
print(check_circle(n1))
