class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
#         for i in range(len(nums)):
#             nums[i] *= nums[i]
#         return sorted(nums)
    
    
        return sorted([i ** 2 for i in nums])