class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # my solution
        nums = nums1 + nums2
        nums.sort()
        
        mid = (len(nums) - 1) // 2
       
        if len(nums) % 2 != 0:
            return float(nums[mid])
        return (float(nums[mid] + nums[mid+1])/2)