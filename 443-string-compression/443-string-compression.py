class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars) == 1:
            return 1
        
        curr = chars[0]
        count = 1
        ans = ""
        
        for i, c in enumerate(chars[1:]):
            
            if c == curr:
                count += 1
            else:
                ans += curr
                if count > 1:
                    ans += str(count)
                curr = c
                count = 1
            if i == len(chars) - 2:
                ans += c
                if count > 1:
                    ans += str(count)
        
        
        for i, c in enumerate(ans):
            chars.insert(i, ans[i])
        
        chars = chars[:len(ans)]
        
        return len(chars)
        