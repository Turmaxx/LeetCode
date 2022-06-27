class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            # return indices if sum of the 2 values is equal to target
            if numbers[i] + numbers[j] == target: return [i+1, j+1]
            # if the sum is greater then the target decrement the second pointer by one since the array is sorted.
            elif numbers[i] + numbers[j] > target: j -= 1
            # else if sum is less than the target increment the first pointer by one since the array is sorted.
            else: i += 1