class Solution:
    def isValid(self, s: str) -> bool:
        
        combos = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        stack = []
        
        for c in s:
            if c in combos.keys():
                stack.append(c)
            else:
                if not stack:
                    return False
                match = stack.pop()
                if combos[match] != c:
                    return False
        
        return True if not stack else False