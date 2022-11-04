class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for i in digits: string += str(i)
        nums = int(string) + 1
        return [int(i) for i in str(nums)]
        