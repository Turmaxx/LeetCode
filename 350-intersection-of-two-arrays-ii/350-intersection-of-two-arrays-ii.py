# class Solution(object):
#     def intersect(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         nums1.sort()
#         nums2.sort()
#         intersect = []
#         i, j = 0, 0
        
#         while (len(nums1) > i and len(nums2) > j):
#             if nums1[i] == nums2[j]:
#                 intersect.append(nums2[j])
#                 i += 1
#                 j += 1
#             elif nums1[i] > nums2[j]:
#                 j += 1
#             elif nums1[i] < nums2[j]:
#                 i += 1
#         return intersect
        
        
# hashMap solution        
class Solution:
    def intersect(self, nums1, nums2):
		if len(nums1) > len(nums2):
			return self.intersect(nums2, nums1)

		hmap1, hmap2 = {n: nums1.count(n) for n in set(nums1)}, {n: nums2.count(n) for n in set(nums2)} 
		result = [] 

		for n in hmap1:
			if n in hmap2:
				result += [n] * min(hmap1[n], hmap2[n])

		return result
    
