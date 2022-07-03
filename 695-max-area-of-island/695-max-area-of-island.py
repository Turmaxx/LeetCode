class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r,c):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1:
                grid[r][c] = 0
                return (1 + dfs(r + 1, c) + 
                            dfs(r - 1, c) +
                            dfs(r, c + 1) +
                            dfs(r, c - 1))
                
            else: return 0
        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
            
        return area
            