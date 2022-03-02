class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        ans = 0
        ec, oc, s = 1, 0, 0
        
        for i in arr:
            s += i
            
            if s % 2 == 1:
                oc += 1
                ans += ec
            else:
                ec += 1
                ans += oc
        
        return ans % ((10 ** 9) + 7)