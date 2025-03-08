class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l,h = 0, m - 1
        while l < h:
            mid = l + (h - l)//2
            if matrix[mid][0] == target: return True
            elif matrix[mid][0] < target:
                if matrix[mid + 1][0] > target: l = h = mid
                else: l = mid + 1
            else: 
                h = mid - 1
        
        row = l
        l, h = 0, n - 1

        while l <=h:
            mid = l + (h - l)//2
            if matrix[row][mid] == target: return True
            elif matrix[row][mid] < target: l = mid + 1
            else: h = mid - 1
        
        return False
