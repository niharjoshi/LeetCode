class Solution:
    
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        total = 0
        
        for i in range(0, rows):
                        
            for j in range(0, cols):
                
                if grid[i][j] == 0:
                    continue
                
                up, down, left, right = 0, 0, 0, 0
                
                if i == 0:
                    up = grid[i][j]
                elif grid[i][j] > grid[i - 1][j]:
                    up = abs(grid[i][j] - grid[i - 1][j])
                
                if i == rows - 1:
                    down = grid[i][j]
                elif grid[i][j] > grid[i + 1][j]:
                    down = abs(grid[i][j] - grid[i + 1][j])
                
                if j == 0:
                    left = grid[i][j]
                elif grid[i][j] > grid[i][j - 1]:
                    left = abs(grid[i][j] - grid[i][j - 1])
                
                if j == cols - 1:
                    right = grid[i][j]
                elif grid[i][j] > grid[i][j + 1]:
                    right = abs(grid[i][j] - grid[i][j + 1])
                                
                # up = grid[i][j] if i == 0 else abs(grid[i][j] - grid[i - 1][j])
                # down = grid[i][j] if i == rows - 1 else abs(grid[i][j] - grid[i + 1][j])
                # left = grid[i][j] if j == 0 else abs(grid[i][j] - grid[i][j - 1])
                # right = grid[i][j] if j == cols - 1 else abs(grid[i][j] - grid[i][j + 1])
                
                total = total + 2 + up + down + left + right
        
        return total