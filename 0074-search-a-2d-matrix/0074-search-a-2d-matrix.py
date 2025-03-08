class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top, bot = 0, m - 1
        low, high = 0, n - 1

        while top <= bot: 
            row = top + (bot - top)//2
            if target > matrix[row][-1]: top = row + 1
            elif target < matrix[row][0]: bot = row - 1
            else: break

        if bot < top: return False

        while low <= high:
            mid = low + (high - low)//2
            if target == matrix[row][mid]: return True
            elif target > matrix[row][mid]: low = mid + 1
            else: high = mid - 1

        return False