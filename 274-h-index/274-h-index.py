class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        c = sorted(citations, reverse=True)
        
        for i in range(len(c)):
            if i + 1 > c[i]:
                return i
        
        return len(c)