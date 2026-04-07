from collections import deque

class FreqStack:
    def __init__(self):
        self.frequency = {}
        self.stacks = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        cur_freq = self.frequency.get(val, 0) + 1
        self.frequency[val] = cur_freq
        if cur_freq > self.max_freq:
            self.max_freq = cur_freq
        self.stacks.setdefault(cur_freq, deque()).append(val)

    def pop(self) -> int:
        val = self.stacks[self.max_freq].pop()
        self.frequency[val] -= 1
        if not self.stacks[self.max_freq]:
            self.max_freq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
