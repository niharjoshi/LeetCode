class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "": return 0
        
        if len(s) == 1: return 1
        
        cache = ""
        ans = 0
        
        for c in s:
            
            if c not in cache:
                
                cache = cache + c
                
                ans = max(ans, len(cache))
            
            else:
                
                pos = cache.find(c)
                
                cache = cache[pos + 1:] + c
                
        return ans