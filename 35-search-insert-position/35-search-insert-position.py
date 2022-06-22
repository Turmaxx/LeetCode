class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # Time Complexity: O(n)
        # nums.append(target)
        # return nums.index(target)
    
        # Time Complexity: O(n)
        # for index, value in enumerate(nums):
        #     if value > target:
        #         return index - 1
        
        
        
        # Time Complexity: O(log(n))
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: left = mid + 1
            else: right = mid
        
        if left == len(nums) - 1 and nums[left] < target: return left + 1
        else: return left