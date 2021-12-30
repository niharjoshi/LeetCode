# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if lists == []: return None
        
        ans = []
        
        for i in range(len(lists)):
            
            while(lists[i] != None):
                ans.append(lists[i].val)
                lists[i] = lists[i].next
        
        ans.sort()
        
        start = curr = ListNode(0, None)
        
        for item in ans:
            curr.next = ListNode(item, None)
            curr = curr.next
        
        return start.next
            
        