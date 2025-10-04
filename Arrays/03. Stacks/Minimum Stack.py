class MinStack:

    def __init__(self):
        self = self
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        output = sorted(set(self.stack))
        return output[0]


minStack = MinStack()

minStack.push(1)
minStack.push(2)
minStack.push(0)
minStack.push(7)
print(minStack.top())
print(minStack.getMin())
