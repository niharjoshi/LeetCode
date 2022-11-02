class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left, right = 0, sum(nums)
        
        for i, j in enumerate(nums):
            left += j
            if left == right:
                return i
            right -= j
        
        return -1