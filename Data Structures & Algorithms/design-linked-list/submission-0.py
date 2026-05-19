class LinkedList:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.next: Optional[LinkedList] = None
        self.prev: Optional[LinkedList] = None

class MyLinkedList:

    def __init__(self):
        self.head = LinkedList()
        self.tail = LinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next

        while cur != self.tail and index > 0:
            cur = cur.next
            index -= 1

        if cur == self.tail:
            return -1

        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = LinkedList(val)

        first = self.head.next

        new_node.prev = self.head
        new_node.next = first

        self.head.next = new_node
        first.prev = new_node

    def addAtTail(self, val: int) -> None:
        new_node = LinkedList(val)

        last = self.tail.prev

        new_node.prev = last
        new_node.next = self.tail

        last.next = new_node
        self.tail.prev = new_node 

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next

        while cur != self.tail and index > 0:
            cur = cur.next
            index -= 1

        if index > 0:
            return

        new_node = LinkedList(val)
        prev_node = cur.prev

        new_node.prev = prev_node
        new_node.next = cur

        prev_node.next = new_node
        cur.prev = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next

        while cur != self.tail and index > 0:
            cur = cur.next
            index -= 1

        if cur == self.tail:
            return

        prev_node = cur.prev
        next_node = cur.next

        prev_node.next = next_node
        next_node.prev = prev_node

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)