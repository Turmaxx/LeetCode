# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]


# Above is the brute force method for finding the two sum of our target value
# BigO : O(n**2)

# We can solve this question using a hashmap
# we loop through the array and subtract the target from our current value and the difference is the value we are looking for
# we the check if the value is in the hashmap if it is we return an array of the 2 indexes (initial value, difference)
# if its not we add the value and the index to our hashmap
# BigO: O(n)


# Neetcode => https://www.youtube.com/watch?v=KLlXCFG5TnA
                    
class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]: 
        prevMap = {}
        for index, value in enumerate(nums):
           difference = target - value
           if difference in prevMap:
               return [index, prevMap[difference]]
           prevMap[value] = index
        return None
