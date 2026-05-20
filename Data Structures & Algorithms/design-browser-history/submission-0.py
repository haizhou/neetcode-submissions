class LL:
    def __init__(self, val: str, prev: Optional(LL) = None, next: Optional(LL) = None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = LL(homepage)
        self.tail = LL(' ')
        self.head = LL(' ')
        self.head.next = self.homepage
        self.homepage.prev = self.head
        self.tail.prev = self.homepage
        self.homepage.next = self.tail
        self.cur = self.homepage
        
    def visit(self, url: str) -> None:
        cur = self.cur
        last = LL(url)
        last.next = self.tail
        self.tail.prev = last
        cur.next = last
        last.prev = cur
        self.cur = last

    def back(self, steps: int) -> str:
        cur = self.cur
        if not cur.prev == self.head:
            while (not cur == self.head) and steps:
                cur = cur.prev
                steps -= 1
            if not steps:
                self.cur = cur
            else:
                self.cur = cur.next
        return self.cur.val
        
    def forward(self, steps: int) -> str:
        cur = self.cur
        if not cur.next == self.tail:
            while (not cur == self.tail) and steps:
                cur = cur.next
                steps -= 1
            if not steps:
                self.cur = cur
            else:
                self.cur = cur.prev
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)