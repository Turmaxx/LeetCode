class Solution:
    def removeHash(self,string):
        stack = []
        for i in string:
            if i != '#':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
        return stack
    
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.removeHash(s) == self.removeHash(t)
            