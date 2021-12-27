class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s == "": return True
        
        if s and t == "": return False
        
        d = {c:0 for c in s}
        
        p = 0
        
        for c in t:
            
            if c == s[p]:
                
                p += 1
            
            if p == len(s): return True

        return False
        