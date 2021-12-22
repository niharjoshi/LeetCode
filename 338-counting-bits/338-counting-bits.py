class Solution:
    def countBits(self, n: int) -> List[int]:
        
        r = [0]
        
        for i in range(1, n + 1):
            
            r.append(r[i & (i - 1)] + 1)
        
        return r