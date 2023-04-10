class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_counts = {}
        
        for n in nums:
            if n in num_counts:
                num_counts[n] += 1
            else:
                num_counts[n] = 1
        
        sorted_counts = sorted([(v, k) for k, v in num_counts.items()], reverse=True)
        
        res = []
        
        for i in range(0, k):
            res.append(sorted_counts[i][1])
        
        return res