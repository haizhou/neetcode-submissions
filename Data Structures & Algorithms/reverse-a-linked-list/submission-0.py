class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        shit = None

        while head:
            piss0 = head.next
            head.next = shit
            shit = head
            head = piss0
    
        return shit