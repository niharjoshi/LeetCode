class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in matrix:

            if target > i[-1]:
                continue
            
            if target < i[-1]:
                left = 0
                right = len(i) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if target > i[mid]:
                        left = mid + 1
                    elif target < i[mid]:
                        right = mid - 1
                    else:
                        return True
            
            else:
                return True