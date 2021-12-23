class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_p = 0
        min_b = float("inf")
        
        for p in prices:
            
            min_b = min(min_b, p)
            max_p = max(max_p, p - min_b)
        
        return max_p
