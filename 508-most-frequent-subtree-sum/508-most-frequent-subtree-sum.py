# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = collections.defaultdict(int)
        
        def traverse(node):
            
            if not node:
                return 0
            
            s = node.val + traverse(node.left) + traverse(node.right)
            
            ans[s] += 1
            
            return s
        
        traverse(root)
        
        mv = max(ans.values())
            
        return [k for k,v in ans.items() if v == mv]