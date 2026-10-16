class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = 1000

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        mini_val = int(self.mini)
        return min(self.stack)
        
