class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1: return [[1]]
                
        t = [[1], [1, 1]]
        
        for i in range(3, numRows + 1):
            
            t.append([1] + ([None] * (i - 2)) + [1])
            
            for j in range(1, int(i / 2) + 1):
                
                t[i - 1][j]= t[i - 1][-j - 1] = t[i - 2][j - 1] + t[i - 2][j]
        
        return t
