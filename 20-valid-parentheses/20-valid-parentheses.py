class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 !=0: return False
        
        if s[0] == ")" or s[0] == "}" or s[0] == "]": return False
        
        mapping = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        stack = ""
        
        for c in s:
                        
            if c == "(" or c == "{" or c == "[":
                stack = stack + c
            
            else:
                
                if len(stack) == 0:
                    return False
                
                elif mapping[stack[-1]] == c:
                    stack = stack[0:-1]
                    
                else:
                    return False
        
        if stack == "":
            return True
        else:
            return False
            
        
        