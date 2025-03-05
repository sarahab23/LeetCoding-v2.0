class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        return

    def push(self, val: int) -> None:
        store = []
        self.stack.append(val)
        while self.minStack and self.minStack[-1] < val:
            store.append(self.minStack.pop())
        self.minStack.append(val)
        for n in store[::-1]:
            self.minStack.append(n)
        return

    def pop(self) -> None:
        removeN = self.stack.pop()
        store = []
        while self.minStack[-1] != removeN:
            store.append(self.minStack.pop())
        self.minStack.pop()
        for n in store[::-1]:
            self.minStack.append(n)
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
