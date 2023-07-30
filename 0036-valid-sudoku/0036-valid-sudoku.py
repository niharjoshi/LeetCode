class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxs = [[set() for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):

                element = board[i][j]

                if element == ".":
                    continue
                
                elif element in rows[i] or element in cols[j] or element in boxs[i // 3][j // 3]:
                    return False
                
                rows[i].add(element)
                cols[j].add(element)
                boxs[i // 3][j // 3].add(element)
        
        return True