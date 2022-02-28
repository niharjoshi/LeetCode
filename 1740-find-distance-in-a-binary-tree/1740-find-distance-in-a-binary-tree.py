# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def find_path(self, node, value, path):
        if not node:
            return False
        path.append(node.val)
        found = False
        if node.val == value:
            found = True
        else:
            found = self.find_path(node.left, value, path) or self.find_path(node.right, value, path)
        if not found:
            path.remove(node.val)
        return found
    
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        if p == q:
            return 0
        
        path_p = []
        path_q = []
        
        self.find_path(root, p, path_p)
        self.find_path(root, q, path_q)
        
        i = 0
        
        while i < len(path_p) and i < len(path_q):
            if path_p[i] != path_q[i]:
                break
            i += 1
        
        result = len(path_p[i:]) + len(path_q[i:])
        
        return result
        