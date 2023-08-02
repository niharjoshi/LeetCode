class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum:
            self.minimum.append(val)
            return None
        if self.minimum and val <= self.minimum[-1]:
            self.minimum.append(val)
        return None

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            if self.minimum and self.minimum[-1] == popped:
                self.minimum.pop()
        return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minimum:
            return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()