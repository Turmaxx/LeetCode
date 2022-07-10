from math import floor

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sorting solution
        # Time: O(nlogn()) Space O(1) or O(n)
        nums.sort()
        return nums[len(nums)//2]            

        # hashmap solution
        # Time: O(n) Space O(n)
        # hMap = Counter(nums)
        # return max(hMap.keys(), key = hMap.get)


        
        # My solution
        # hMap = Counter(nums)
        # great, element = hMap[nums[0]], nums[0] 
        # for key in hMap:
        #     if great < hMap[key]:
        #         element = key
        # return element