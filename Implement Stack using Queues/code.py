class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def add(self, item):
        if not self.is_empty():
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(item)
        else:
            self.head = Node(item)
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node.value

    def peek(self):
        return self.head.value if self.head is not None else None

    def __len__(self):
        return self.size

class MyStack:
    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.add(x)
        for _ in range(len(self.queue) - 1):
            elem = self.queue.pop()
            self.queue.add(elem)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.is_empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
