class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if nums == []: return []
                
        for i in range(0, len(nums) - 1):
            
            req = target - nums[i]
            
            for j in range(i + 1, len(nums)):
                
                if nums[j] != req:
                    
                    continue
                
                elif nums[j] == req:
                    
                    return [i, j]