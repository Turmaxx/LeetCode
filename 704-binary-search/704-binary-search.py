class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums: return -1
        
        left, right = 0, len(nums) - 1
        
        def recursiveBinarySearch(array, target, left, right):
            mid = left + (right - left) // 2
            if array[mid] == target: return mid
            elif array[mid] > target: return recursiveBinarySearch(array, target, left, mid-1)
            else: return recursiveBinarySearch(array, target, mid + 1, right)
            
        # return -1 if target not in nums else recursiveBinarySearch(nums, target, left, right)
        return recursiveBinarySearch(nums, target, left, right)