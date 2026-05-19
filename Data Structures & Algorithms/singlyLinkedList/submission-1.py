class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next: Optional[ListNode] = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        cur = self.head

        while index > 0 and cur:
            cur = cur.next
            index -= 1

        if cur is None:
            return -1

        return cur.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return True

        cur = self.head

        for _ in range(index - 1):
            if cur is None:
                return False
            cur = cur.next

        if cur is None or cur.next is None:
            return False

        if cur.next == self.tail:
            self.tail = cur

        cur.next = cur.next.next

        return True

    def getValues(self) -> List[int]:
        arr = []
        cur = self.head

        while cur:
            arr.append(cur.val)
            cur = cur.next

        return arr
