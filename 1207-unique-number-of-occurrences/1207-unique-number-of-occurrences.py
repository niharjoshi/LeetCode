class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        if len(arr) == 1:
            return True
        
        occurences = {}
        
        for item in arr:
            
            if item in occurences:
                occurences[item] += 1
            
            else:
                occurences[item] = 1
        
        if len(occurences.values()) == len(set(occurences.values())):
            return True
        else:
            return False
            
            
        