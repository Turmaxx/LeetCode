class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        columns = len(matrix[0])
        left, right = 0, (len(matrix) * columns) - 1
        
        while left <= right:
            middle = (left + right) // 2
            row, column = middle // columns, middle % columns

            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                right = middle - 1
            else:
                left = middle + 1
                
        return False

    
        