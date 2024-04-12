# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(start):

            prev = None
            curr = start

            while curr:
                n = curr.next
                curr.next = prev
                prev = curr
                curr = n
            
            return prev
        
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        rev = reverse(slow.next)
        slow.next = None

        while rev:
            l = head.next
            r = rev.next
            head.next = rev
            rev.next = l
            rev = r
            head = l