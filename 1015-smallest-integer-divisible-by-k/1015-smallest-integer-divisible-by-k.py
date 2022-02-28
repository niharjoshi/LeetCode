class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        k -> +ve int
        n -> smallest +ve int such that n % k == 0, only contains 1s
        ans -> len(n) or -1
        
        Examples:
        
        k = 3, n = (1, 1), (11, 2), (111, 0)
        k = 7, n = (1, 1), (11, 4), (111, 6), (1111, 5), (11111, 2), (111111, 0), (1111111, 1), (11111111, 4)
        """
        
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        n = 1
        n_counter = 1
        
        repeated = {}
        
        remainder = -1
        
        while n < k:
            n = n * 10 + 1
            n_counter += 1
        
        for i in range(k):
            
            remainder = n % k
            
            if remainder == 0:
                return n_counter
            
            if remainder in repeated:
                return -1
            else:
                repeated[remainder] = 0
            
            n = n * 10 + 1
            n_counter += 1
        
        return -1