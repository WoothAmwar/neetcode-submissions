class MinStack:

    def __init__(self):
        self.curr_min = (2**31)-1
        self.stack_len = 0
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.curr_min:
            self.curr_min = val
            self.min_stack.append(val)
        self.stack_len += 1

    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            if len(self.min_stack) > 1:
                self.curr_min = self.min_stack[-2]
            else:
                self.curr_min = float('inf')
            self.min_stack.pop(-1)
        self.stack.pop(-1)
        self.stack_len -= 1        

    def top(self) -> int:
        return self.stack[self.stack_len-1]

    def getMin(self) -> int:
        return self.curr_min
