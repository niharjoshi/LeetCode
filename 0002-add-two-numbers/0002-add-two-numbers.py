# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(start):

            prev = None
            curr = start

            while curr:
                n = curr.next
                curr.next = prev
                prev = curr
                curr = n
            
            return prev
        
        h1, h2 = reverse(l1), reverse(l2)
        n1, n2 = 0, 0

        while h1 or h2:
            if h1:
                n1 = (n1 * 10) + h1.val
                h1 = h1.next
            if h2:
                n2 = (n2 * 10) + h2.val
                h2 = h2.next
        
        n = n1 + n2
        print(n)

        if n == 0:
            return ListNode(n)
        
        start = ListNode()
        head = start

        while n != 0:
            num = n % 10
            n = n // 10
            start.next = ListNode(num)
            start = start.next
    
        return head.next