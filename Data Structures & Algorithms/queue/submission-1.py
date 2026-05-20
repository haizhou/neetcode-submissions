class set:
    def __init__(self, val: int = 0, right: set() = None, left: set() = None) -> None:
        self.val = val
        self.right = right
        self.left = left

class Deque:
    
    def __init__(self):
        self.head = set()
        self.tail = set()
        self.head.right = self.tail
        self.tail.left = self.head

    def isEmpty(self) -> bool:
        return self.head.right == self.tail
        
    def append(self, value: int) -> None:
        cur = set(value)
        if self.isEmpty():
            self.head.right = cur
            cur.left = self.head
            self.tail.left = cur
            cur.right = self.tail
        else:
            cur1 = self.tail.left
            cur1.right = cur
            cur.left = cur1
            cur.right = self.tail
            self.tail.left = cur
        

    def appendleft(self, value: int) -> None:
        cur = set(value)
        if self.isEmpty():
            self.head.right = cur
            cur.left = self.head
            self.tail.left = cur
            cur.right = self.tail
        else:
            cur1 = self.head.right
            cur1.left = cur
            cur.right = cur1
            cur.left = self.head
            self.head.right = cur
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        cur = self.tail.left
        before = cur.left
        before.right = self.tail
        self.tail.left = before
        return cur.val
        


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        cur = self.head.right
        after = cur.right
        after.left = self.head
        self.head.right = after
        return cur.val