class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        curr = 0
        start = 0
        count = 0
        
        for end, item in enumerate(nums):
            
            if left <= item <= right:
                curr = end - start + 1
            
            elif item > right:
                curr = 0
                start = end + 1
            
            count += curr
        
        return count