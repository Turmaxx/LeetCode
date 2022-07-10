class Solution:
    def bsearch(self, nums, target, found):
        low, high = 0, len(nums) - 1
        
        index = -1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if nums[mid] == target:
                index = mid
                if found: high = mid - 1
                else: low = mid + 1
            elif nums[mid] < target: low = mid + 1
            else: high = mid - 1             
            
        return index
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:        
        if target not in nums or len(nums) == 0: return [-1,-1]
        
        index1 = self.bsearch(nums, target, True)    
        index2 = self.bsearch(nums, target, False)
    
        return [index1, index2] 