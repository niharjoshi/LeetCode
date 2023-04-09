class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if len(nums) == 0 or len(nums) == 1:
            return False
        
        visited = {}
        
        for item in nums:
            if item in visited.keys():
                return True
            visited[item] = 1
        
        return False