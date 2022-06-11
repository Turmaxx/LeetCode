class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for index, char in enumerate(s):
            if s.count(char) == 1:
                return index
        return -1