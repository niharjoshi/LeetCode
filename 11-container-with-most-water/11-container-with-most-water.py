class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        if len(height) == 2: return min(height)
        
        left = 0
        right = len(height) - 1
        ans = 0
        
        for i in range(0, len(height)):
            
            h = min(height[left], height[right]) * (right - left)
            
            ans = max(ans, h)
            
            if height[left] <= height[right]:
                left += 1
            
            else:
                right -= 1
        
        return ans
        