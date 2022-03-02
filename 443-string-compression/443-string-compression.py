class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars) == 1:
            return 1
        
        ans = ""
        count = 0
        curr = chars[0]
        
        for c in chars:
            
            if c == curr:
                count += 1
            else:
                ans += curr
                curr = c
                if count > 1:
                    ans += str(count)
                count = 1
        
        ans += curr
        if count > 1:
            ans += str(count)
        
        for i in range(len(ans)):
            chars.insert(i, ans[i])
        
        chars = chars[:len(ans)]
        
        return len(chars)