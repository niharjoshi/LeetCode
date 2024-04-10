class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[left] == nums[mid] or nums[right] == nums[mid]:
                return min(nums[left], nums[right])
            elif nums[left] < nums[mid] < nums[right]:
                return nums[left]
            elif nums[left] > nums[mid] < nums[right]:
                right = mid
            elif nums[left] < nums[mid] > nums[right]:
                left = mid
        