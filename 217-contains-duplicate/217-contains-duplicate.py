class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums_set = set(nums)
        return False if len(nums_set) == len(nums) else True