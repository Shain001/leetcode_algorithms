"""
两个栈实现队列的delete head and append to tail
"""


class Queue:
    def __init__(self):
        self.tails = []
        self.heads = []

    def append_to_tail(self, value):
        self.tails.append(value)

    def delete_head(self):
        if len(self.heads) == 0 and len(self.tails) == 0:
            return "Empty"
        if len(self.heads) == 0:
            while len(self.tails) != 0:
                self.heads.append(self.tails.pop(-1))

        return self.heads.pop(-1)


class Stack:
    """
        两个队列实现queue
    """
    def __init__(self):
        self.to_save = []
        self.to_delete_save = []

    def push(self,value):
        self.to_save.append(value)
        return "pushed"

    def pop(self):
        if len(self.to_delete_save) == 0 and len(self.to_save) == 0:
            return "Empty"
        while len(self.to_save) != 1:
            self.to_delete_save.append(self.to_save.pop(0))
        to_return = self.to_save.pop()
        self.to_save = self.to_delete_save
        self.to_delete_save = []
        return to_return

q = Stack()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

