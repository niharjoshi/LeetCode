# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_len = [root.val]

        def dfs(r):

            if not r:
                return 0
            
            left_path = dfs(r.left)
            right_path = dfs(r.right)

            left_path = max(left_path, 0)
            right_path = max(right_path, 0)

            max_len[0] = max(max_len[0], r.val + left_path + right_path)

            return r.val + max(left_path, right_path)
        
        dfs(root)

        return max_len[0]