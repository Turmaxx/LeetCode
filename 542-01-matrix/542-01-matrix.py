class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        visited = set()
        q = []
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))
                    
        
        dirc = [(1,0) , (0,1) , (0,-1) , (-1,0)]
        
        while q:
            x , y = q[0]
            
            for i,j in dirc:
                new_x = x+i
                new_y = y+j
                if 0 <= new_x < len(mat) and 0 <= new_y < len(mat[0]) and (new_x,new_y) not in visited:
                    mat[new_x][new_y] = 1 + mat[x][y]
                    
                    visited.add((new_x,new_y))
                    q.append((new_x,new_y))
                    
            q.pop(0)
                    
        return mat