class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low, high = 0, len(nums) - 1
        res = nums[0]
        
        if high + 1 == 1: return res
        
        while low <= high:
            if nums[low] < nums[high]:
                res = min(res, nums[low])
                break
            mid = (low + high) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[low]: low = mid + 1
            else: high = mid - 1
                
        return res