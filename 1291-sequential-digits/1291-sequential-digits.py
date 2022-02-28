class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        sequence = "123456789"
        max_n = 10
        ans = []
        
        for i in range(len(str(low)), len(str(high)) + 1):
            for j in range(max_n - i):
                num = int(sequence[j:j + i])
                if num >= low and num <= high:
                    ans.append(num)
        
        return ans