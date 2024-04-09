class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        visited = {}
        length = 0
        res = 0

        for r in range(len(s)):
            
            visited[s[r]] = visited.get(s[r], 0) + 1
            length += 1
            maximum = visited[max(visited, key=visited.get)]

            if (length - maximum) <= k:
                res = max(res, length)
            else:
                visited[s[l]] -= 1
                l += 1
                length -= 1
        
        return res

