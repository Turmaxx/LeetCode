class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Solution https://www.youtube.com/watch?v=gqXU1UyA8pk
        char = set()
        left = 0
        result = 0
        
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left += 1
            char.add(s[right])
            result = max(result, right - left + 1)
            
        return result
        