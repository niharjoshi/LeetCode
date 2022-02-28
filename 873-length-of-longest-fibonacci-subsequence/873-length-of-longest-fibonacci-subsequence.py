class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        
        """
        
        if len(arr) == 1 or len(arr) == 2:
            return 0
        
        s = set(arr)
        res = -1
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                x, y = arr[j], arr[i] + arr[j]
                length = 2
                
                while y in s:
                    x, y = y, x + y
                    length += 1
                
                res = max(res, length)
                
        return res if res >= 3 else 0