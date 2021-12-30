class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if nums == []: return []
                
        dp = {}
        
        for i in range(0, len(nums)):
            
            req = target - nums[i]
            
            if req in dp:
                return [i, dp[req]]
            
            dp[nums[i]] = i
