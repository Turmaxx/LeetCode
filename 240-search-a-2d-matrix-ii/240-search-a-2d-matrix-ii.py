class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
#         for sub in matrix:
#             sub.sort()
            
#         for sub in matrix:
#             if target in sub: return True
        
#         return False

        M, N = len(matrix), len(matrix[0])
        i, j = 0, N - 1
        
        while i < M and j >= 0:
            if target == matrix[i][j]: return True
            elif target < matrix[i][j]: j -= 1
            else: i += 1
            
        return False
        