class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        max_streak = 0
        
        while nums:
            
            low = high = nums.pop()
            current_streak = 1
            
            while (low - 1) in nums:
                nums.remove(low - 1)
                current_streak += 1
                low -= 1
            
            while (high + 1) in nums:
                nums.remove(high + 1)
                current_streak += 1
                high += 1
                        
            max_streak = max(max_streak, current_streak)
        
        return max_streak