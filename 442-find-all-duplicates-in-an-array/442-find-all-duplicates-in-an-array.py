class Solution(object):
    def findDuplicates(self, nums):    
        res = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                res.append(abs(i))
            else:
                nums[abs(i)-1] = -nums[abs(i)-1]
        return res
    
        