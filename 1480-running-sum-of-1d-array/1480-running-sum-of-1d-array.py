class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        total = 0
        
        for i, j in enumerate(nums):
            total += j
            nums[i] = total
        
        return nums