class Solution:
    def decodeString(self, s: str) -> str:
        
        ans = ""
        num = 0
        
        stack = []
        
        for c in s:
            if c in "0123456789":
                num = num * 10 + int(c)
            elif c == "[":
                stack.append(num)
                stack.append(ans)
                num = 0
                ans = ""
            elif c == "]":
                string = stack.pop()
                multiplier = stack.pop()
                ans = string + int(multiplier) * ans
            else:
                ans += c
        
        return ans