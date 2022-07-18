class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, curr = 0, len(nums) - 1, 0
        
        def swap(i: int , j: int) -> None:
            nums[i], nums[j] = nums[j], nums[i]
            
        
        while curr <= right:
            if nums[curr] == 0:
                swap(curr, left)
                curr += 1
                left += 1
            elif nums[curr] == 1: 
                curr += 1
            else:
                swap(curr, right)
                right -= 1
        