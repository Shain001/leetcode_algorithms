"""
    逆波兰表达式计算： 从左向右取符号， 计算符号左侧两个数，直至算法
    e.g. 1+(2-3*4)/5+6  --> 1234*-5/+6+
"""
from stack import *


def calculate(string):
    if string is None:
        return "error"

    string = string.split(',')
    nums = Stack()
    num1, num2 = None, None
    for ch in string:
        if ch.isdigit():
            nums.push(ch)
        elif ch == '+':
            num1 = nums.pop()
            num2 = nums.pop()
            nums.push(int(num2)+int(num1))
        elif ch == '-':
            num1 = nums.pop()
            num2 = nums.pop()
            nums.push(int(num2)-int(num1))
        elif ch == '*':
            num1 = nums.pop()
            num2 = nums.pop()
            nums.push(int(num2)*int(num1))
        elif ch == '/':
            num1 = nums.pop()
            num2 = nums.pop()
            nums.push(int(num2)/int(num1))
    return nums.pop()


def convert_to_rpn(string):
    """
    (1) 初始化两个栈：运算符栈S1和储存中间结果的栈S2；
    (2) 从左至右扫描中缀表达式；
    (3) 遇到操作数时，将其压入S2；
    (4) 遇到运算符时，比较其与S1栈顶运算符的优先级：
    (4-1) 如果S1为空，或栈顶运算符为左括号“(”，则直接将此运算符入栈；
    (4-2) 否则，若优先级比栈顶运算符的高，也将运算符压入S1（注意转换为前缀表达式时是优先级较高或相同，而这里则不包括相同的情况）；
    (4-3) 否则，将S1栈顶的运算符弹出并压入到S2中，再次转到(4-1)与S1中新的栈顶运算符相比较；
    (5) 遇到括号时：
    (5-1) 如果是左括号“(”，则直接压入S1；
    (5-2) 如果是右括号“)”，则依次弹出S1栈顶的运算符，并压入S2，直到遇到左括号为止，此时将这一对括号丢弃；
    (6) 重复步骤(2)至(5)，直到表达式的最右边；
    (7) 将S1中剩余的运算符依次弹出并压入S2；
    (8) 依次弹出S2中的元素并输出，结果的逆序即为中缀表达式对应的后缀表达式（转换为前缀表达式时不用逆序）。

    :param string:
    :return:
    """
    string = string.split(" ")
    nums, ops = Stack(), Stack()
    priorities = {
        '+' : 0,
        '-' : 0,
        '*' : 1,
        '/' : 1,
        '(' : 2
    }
    for ch in string:
        if ch.isdigit():
            nums.push(ch)
        else:
            if ch != ')':
                if ops.count == 0:
                    ops.push(ch)
                else:
                    top = ops.head.next.value
                    if top == '(':
                        ops.push(ch)
                    else:
                        # '当前优先级小于等于'栈顶优先级则先将栈顶运算符压入Nums, 这样则可保证高优先级先被运算且同级之间运算符顺序不变
                        while priorities[ch] <= priorities[top] and ops.count != 0:
                            nums.push(ops.pop())
                            if ops.head.next is not None:
                                top = ops.head.next.value
                            if top == '(':
                                break
                        ops.push(ch)
            else:
                top = ops.head.next.value
                while top != '(':
                    nums.push(ops.pop())
                    top = ops.head.next.value
                # 弹出左括号
                ops.pop()
    while ops.count != 0:
        nums.push(ops.pop())

    result = []
    while nums.count != 0:
        result.append(str(nums.pop()))
    result.reverse()
    return ''.join(result)


def compute(string):
    rpn = convert_to_rpn(string)
    result = calculate(rpn)
    return result


print(calculate('1,2,3,+,4,*,+,5,-'))
