class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append([val, min(self.stack[-1][1], val) if self.stack else val]) 
        return       

    def pop(self) -> None:
        if self.stack: self.stack.pop()
        return

    def top(self) -> int:
        if self.stack: return self.stack[-1][0]
        return

    def getMin(self) -> int:
        if self.stack: return self.stack[-1][1]
        return


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()