class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1
        
        while nums[low] != target or nums[high] != target:
            if nums[low] != target: low += 1
            if nums[high] != target: high -= 1
            
        return [low, high]
    
    def searchRange(self, nums, target):
        if target not in nums or len(nums) == 0: return [-1,-1]
        return self.search(nums, target)