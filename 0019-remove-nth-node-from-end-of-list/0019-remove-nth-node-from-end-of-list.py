# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        start = 0
        trav = head

        while trav:
            start += 1
            trav = trav.next
        
        if start == 1:
            head = None
            return head
        elif start == n:
            head = head.next
            return head

        curr = head

        for i in range(start - n - 1):
            curr = curr.next
        
        if n == 1:
            curr.next = None
        else:
            curr.next = curr.next.next
        
        return head