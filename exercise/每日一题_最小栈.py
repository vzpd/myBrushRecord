class MinStack:

    def __init__(self):
        self.arr = []
        self.minArr = []

    def push(self, x: int) -> None:
        self.arr.append(x)
        if self.minArr:
            self.minArr.append(x if x < self.minArr[-1] else self.minArr[-1])
        else:
            self.minArr.append(x)

    def pop(self) -> None:
        self.minArr.pop(-1)
        return self.arr.pop(-1)

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minArr[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert minStack.getMin() == -3
minStack.pop()
assert minStack.top() == 0
assert minStack.getMin() == -2
