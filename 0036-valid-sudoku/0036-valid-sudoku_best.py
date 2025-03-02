class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # store all elts with rows in common
        cols = defaultdict(set) # store all elts with columns in common
        squares = defaultdict(set) # store all elts with squares in common
        # or collections.defaultdict(set)

        # when going through each posn, we check what's common for all elts belonging to a row
        # when going through each posn, we check what's common for all elts belonging to a col
        # when going through each posn, we check what's common for all elts belonging to a square: 0,1,2 -> divided by 3 gives 0 || 3,4,5 -> divided by 3 gives 1 ||
        # 6,7,8 -> divided by 2 gives 0 
        #    0    1     2
        #  0
        #  1
        #  2
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or
                 board[r][c] in squares[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
            
        return True
