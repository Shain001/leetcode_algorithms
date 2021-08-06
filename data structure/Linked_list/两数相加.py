"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""
import linked_list


def two_nums_sum(li1, li2):
    node_li1 = li1.head.next
    node_li2 = li2.head.next
    result = linked_list.LinkedList()
    carry = 0
    while node_li1 is not None or node_li2 is not None:
        if node_li2 is not None and node_li1 is not None:
            sum_temp = node_li1.value + node_li2.value + carry
        elif node_li2 is not None and node_li1 is None:
            sum_temp = node_li2.value + carry
        else:
            sum_temp = node_li1.value + carry

        item = sum_temp % 10
        carry = sum_temp // 10
        result.append(item)

        if node_li1 is not None:
            node_li1 = node_li1.next
        if node_li2 is not None:
            node_li2 = node_li2.next

    if carry != 0:
        result.append(1)

    return result


def entry(l1, l2):
    li1, li2 = linked_list.LinkedList(), linked_list.LinkedList()
    for i in l1:
        li1.append(i)
    for i in l2:
        li2.append(i)
    return two_nums_sum(li1, li2)


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
print(entry(l1, l2))



