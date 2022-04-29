class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        i, j = 0, len(strX) - 1
        
        while i < len(strX):
            if strX[i] != strX[j]:
                return False
            i+=1
            j-=1
            
            
        return True