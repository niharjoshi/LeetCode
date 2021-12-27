class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if nums == []: return 0
        
        if len(nums) == 1: return nums[0]
        
        b = c = nums[0]
        
        for i in range(1, len(nums)):
            
            c = max(nums[i], c + nums[i])
            
            if b < c:
                b = c
        
        return b
        