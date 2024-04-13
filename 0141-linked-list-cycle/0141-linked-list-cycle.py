# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Solution 1
        # if not head:
        #     return False
        # slow = head
        # fast = head.next
        # while fast and fast.next:
        #     if slow == fast:
        #         return True
        #     slow = slow.next
        #     fast = fast.next.next
        # return False

        # Solution 2
        # visited = set()
        # while head:
        #     if head in visited:
        #         return True
        #     visited.add(head)
        #     head = head.next
        # return False

        # Solution 3
        while head:
            if head.val is None:
                return True
            head.val = None
            head = head.next
        return False