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
        
        while self.cur.prev != self.head and steps > 0:
            self.cur = self.cur.prev
            steps -= 1

        return self.cur.val
        
    def forward(self, steps: int) -> str:
        while self.cur.next != self.tail and steps > 0:
            self.cur = self.cur.next
            steps -= 1

        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)