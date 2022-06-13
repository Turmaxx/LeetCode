class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        intersect = []
        i, j = 0, 0
        
        while (len(nums1) > i and len(nums2) > j):
            if nums1[i] == nums2[j]:
                intersect.append(nums2[j])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
        return intersect
        