class Solution(object):
    def isValid(self,s):
        """
        :type s: str
        :rtype: bool
        """
        opening_brackets = "{(["
        closing_brackets = "})]"
        is_valid = False

        for i in range(len(s)):
            if s[i] in opening_brackets:
                for j in range(i, len(s)):
                    if s[j] in closing_brackets:
                        is_valid = True
                        
            elif s[i]:
                return False

        return is_valid
            


test = Solution()
print(test.isValid("()"))