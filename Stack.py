class Stack:
    def __init__(self):
        self.stack = []
        self.my_min = []

    def push(self, val):
        self.stack.append(val)

        # record to my_min
        self.my_min.append(val)
        self.my_min.sort()
        # record min value
        if self.my_min is None:
            self.my_min = val

    def pop(self):
        if len(self.stack) == 0:
            return "Empty Stack"

        to_return = self.stack.pop(-1)

        i = 0
        while True:
            if self.my_min[i] == to_return:
                self.my_min.pop(i)
                break
            i += 1

        self.my_min.sort()

        return to_return

    def show_min(self):
        return self.my_min[0]


stack_my = Stack()
stack_my.push(5)
stack_my.push(4)

print(stack_my.show_min())
stack_my.push(3)
stack_my.pop()
print(stack_my.show_min())
stack_my.pop()

stack_my.push(2)
print(stack_my.show_min())
stack_my.push(1)
stack_my.pop()
