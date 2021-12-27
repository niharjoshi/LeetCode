class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0: return 0
        
        if n == 1: return 1
        
        ans = [0, 1]
        
        for i in range(2, n + 1):
            
            ans.append(ans[i - 2] + ans[i - 1])
            
        return ans[n]
