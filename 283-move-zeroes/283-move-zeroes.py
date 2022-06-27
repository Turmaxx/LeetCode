class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Time Complexity O(n)
        # Space Complexity O(1)
        # Solution: https://www.youtube.com/watch?v=aayNRwUN3Do
        
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1