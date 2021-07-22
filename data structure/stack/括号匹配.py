"""
    使用栈检测括号是否匹配
"""

import stack

def check_brackets(string):
    st = stack.Stack()
    for ch in string:
        if ch == '(':
            st.push(ch)
        elif ch == ')':
            if st.pop() == "empty":
                return False
    if st.check_empty():
        return True
    else:
        return False


print(check_brackets("(((2(()3)))"))

