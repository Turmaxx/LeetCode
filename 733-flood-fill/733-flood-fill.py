class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image == None or image[sr][sc] == color: return image
        self.fill(image, sr, sc, image[sr][sc], color)
        return image
            
        
        
    def fill(self, image, r, c, initial, newColor):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != initial: return
    
        image[r][c] = newColor
        
        self.fill(image, r+1, c, initial, newColor) #down
        self.fill(image, r-1, c, initial, newColor) #up
        self.fill(image, r, c+1, initial, newColor) #left
        self.fill(image, r, c-1, initial, newColor) #right