class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n = len(s1)
        m = len(s2)
        
        if n == 0 or m == 0: return False
        
        if m > m: return False
        
        def createIndex(str: string) -> dict:
            index = {}
            for c in str:
                if c not in index:
                    index[c] = 1
                else:
                    index[c] += 1
            return index
        
        s1_hash = sum([hash(i) for i in s1])
        
        for i in range(0, m):
             if i + n <= m:
                s2_hash = sum([hash(j) for j in s2[i:i + n]])
                if s2_hash == s1_hash:
                    return True
        
        return False
    