"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        curr = head
        visited = {}

        while curr:
            visited[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            visited[curr].next = visited.get(curr.next)
            visited[curr].random = visited.get(curr.random)
            curr = curr.next
        
        return visited[head]
        
