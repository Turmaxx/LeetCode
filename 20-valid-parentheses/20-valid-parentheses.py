class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) % 2 != 0: return False
        
        closetoOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        
        stack = []
    
        for i in s:
            if i in closetoOpen:
                if stack and stack[-1] == closetoOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        return True if not stack else False
        
        
                
            
        
        