class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        index = {}
        
        for word in s1.split(" "):
            if word not in index:
                index[word] = 1
            else:
                index[word] += 1
        
        for word in s2.split(" "):
            if word not in index:
                index[word] = 1
            else:
                index[word] += 1
        
        return [item for item in index if index[item] == 1]
    