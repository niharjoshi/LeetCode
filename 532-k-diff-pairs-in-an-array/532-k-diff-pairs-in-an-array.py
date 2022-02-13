class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 0 or len(nums) == 1:
            return 0
        
        index = dict()
        
        for item in nums:
            if item not in index.keys():
                index[item] = 1
            else:
                index[item] += 1
        
        processed = set()
        
        res = 0
        
        if k == 0:
            for item in index.keys():
                if index[item] > 1:
                    res += 1
        else:
            for item in index.keys():
                if item not in processed:
                    if item + k in index.keys():
                        res += 1
                        processed.add(item)
        
        return res
    