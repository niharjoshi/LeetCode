class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        
        l, r = 0, 1
        visited = set()
        visited.add(s[l])
        len_max = 1
        curr_max = 1

        while r < len(s):

            if s[r] in visited:
                l += 1
                r = l + 1
                visited.clear()
                visited.add(s[l])
                curr_max = 1
            else:
                visited.add(s[r])
                curr_max += 1
                r += 1
            
            len_max = max(len_max, curr_max)
        
        return len_max