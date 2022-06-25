# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n, firstVersion=1):
        """
        :type n: int
        :rtype: int
        """
        # Iterative Approach
        # for i in range(n):
        #     if isBadVersion(i):
        #         return i
        # return -1
        
        # Binary Search Approach
        # left, right = 1, n
        # while left <= right:
        #     mid = left + right // 2
        #     if isBadVersion(mid):
        #         right = mid - 1
        #     else:
        #         left = mid - 1
        # return mid
            
        # Binary Search Recursive Approach
        if n == firstVersion: return n
        mid = (n + firstVersion) // 2
        if isBadVersion(mid): return self.firstBadVersion(mid, firstVersion)
        else: return self.firstBadVersion(n, mid+1)