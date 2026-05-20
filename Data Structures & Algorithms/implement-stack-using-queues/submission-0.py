class Node:
    def __init__(self, val: int =0, next: Node() = None, prev: Node() = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyStack:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, x: int) -> None:
        cur = Node(x)
        after = self.head.next
        cur.prev = self.head
        self.head.next = cur
        cur.next = after
        after.prev = cur

    def pop(self) -> int:
        if self.head.next != self.tail:
            cur = self.head.next
            after = cur.next
            after.prev = self.head
            self.head.next = after
            return cur.val
        

    def top(self) -> int:
        if self.head.next != self.tail:
            return self.head.next.val
        

    def empty(self) -> bool:
        return self.head.next == self.tail
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()