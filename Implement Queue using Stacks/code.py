class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node.value

    def peek(self):
        return self.head.value if self.head is not None else None

    def __len__(self):
        return self.size

class MyQueue:
    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()

    def push(self, x: int) -> None:
        self.instack.push(x)

    def move(self):
        if self.outstack.is_empty():
            while not self.instack.is_empty():
                self.outstack.push(self.instack.pop())

    def pop(self) -> int:
        self.move()
        return self.outstack.pop()

    def peek(self) -> int:
        self.move()
        return self.outstack.peek()

    def empty(self) -> bool:
        return self.instack.is_empty() and self.outstack.is_empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
