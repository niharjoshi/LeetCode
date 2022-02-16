class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        n, m = len(s), len(t)
        
        if n == 1 and m == 1:
            return s == t
        
        tally = {}
        
        for i in range(n):
            if s[i] not in tally:
                tally[s[i]] = 1
            else:
                tally[s[i]] += 1
        
        for i in range(m):
            if t[i] not in tally:
                return False
            else:
                tally[t[i]] -= 1
                if tally[t[i]] == 0:
                    del tally[t[i]]
        
        if tally == {}:
            return True
        else:
            return False