class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # built-in python function called sorted()
        # sorts an sortable data type such as this string and returns a list.
        # we join that list to convert back to a string then we compare if they are equal or not
        return "".join(sorted(s)) == "".join(sorted(t))
        