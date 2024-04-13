# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        def calculate_max_height(start):

            if not start:
                return 0
            
            print(start.val)
            left_depth = 1 + calculate_max_height(start.left)
            right_depth = 1 + calculate_max_height(start.right)

            return max(left_depth, right_depth)
        
        left_height = calculate_max_height(root.left)
        right_height = calculate_max_height(root.right)

        if abs(left_height - right_height) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False