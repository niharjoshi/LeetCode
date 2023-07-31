class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_vol = 0
        
        start = 0
        end = len(height) - 1
        
        while start < end:
            
            curr_vol = min(height[start], height[end]) * abs(start - end)
            max_vol = max(max_vol, curr_vol)
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            
        return max_vol