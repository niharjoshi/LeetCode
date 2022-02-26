class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        
        result = []
        
        previous = "A"
        
        for item in seq:
            
            if item == "(":
                
                if previous == "A":
                    result.append(1)
                    previous = "B"
                else:
                    result.append(0)
                    previous = "A"
            
            else:
                
                if previous == "A":
                    result.append(0)
                    previous = "B"
                else:
                    result.append(1)
                    previous = "A"
        
        return result