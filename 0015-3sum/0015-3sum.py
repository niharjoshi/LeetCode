import itertools

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        
        pos, neg, zer = list(), list(), list()
        
        for item in nums:
            if item == 0:
                zer.append(item)
            elif item < 0:
                neg.append(item)
            else:
                pos.append(item)
        
        p, n = set(pos), set(neg)
        
        if zer:
            for item in p:
                if -1 * item in n:
                    ans.add(tuple([-1 * item, 0, item]))
        
        if len(zer) >= 3:
            ans.add(tuple([0, 0, 0]))
        
        for item in list(itertools.combinations(pos, 2)):
            if -1 * (item[0] + item[1]) in n:
                ans.add(tuple(sorted([item[0], item[1], -1 * (item[0] + item[1])])))
        
        for item in list(itertools.combinations(neg, 2)):
            if -1 * (item[0] + item[1]) in p:
                ans.add(tuple(sorted([item[0], item[1], -1 * (item[0] + item[1])])))
        
        return ans