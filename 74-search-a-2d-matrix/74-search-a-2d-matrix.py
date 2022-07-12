class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        r, c = 0, N - 1
        
        while r < M and c > -1:
            if matrix[r][c] == target: return True;
            elif matrix[r][c] > target: c -= 1
            else: r += 1
        
        return False

    
        # return any(target in sub for sub in matrix)