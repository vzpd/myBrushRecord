# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
# 示例:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.

class MinStack:

    def __init__(self):
        self.dp = []
        self.minIndex = None

    def push(self, x: int) -> None:
        if self.minIndex is not None and x < self.dp[self.minIndex]:
            self.minIndex = len(self.dp)
        self.dp.append(x)

    def pop(self) -> None:
        if self.minIndex == len(self.dp) - 1:
            self.minIndex = None
        self.dp = self.dp[:-1]

    def top(self) -> int:
        return self.dp[-1] if self.dp else None

    def getMin(self) -> int:
        if not self.dp:
            return None
        elif self.minIndex is None:
            minVal = self.dp[0]
            self.minIndex = 0
            for i in range(1, len(self.dp)):
                if self.dp[i] < minVal:
                    minVal = self.dp[i]
                    self.minIndex = i
            return minVal
        else:
            return self.dp[self.minIndex]


minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
assert minStack.getMin() == -3.
minStack.pop();
assert minStack.top() == 0
assert minStack.getMin() == -2

minStack = MinStack()
minStack.push(-10)
minStack.push(14)
minStack.push(-20)
minStack.pop()
minStack.push(10)
minStack.push(-7)
assert minStack.getMin() == -10
