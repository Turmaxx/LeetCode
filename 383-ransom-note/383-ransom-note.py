class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # make a hashmap (char, count)
        # loop through ransomeNote
        # check if the char is not in magazineMap if not return False
        # else decrement magazineMap[i] count by 1
        # after all check are complete means that we can make a ransomeNot from magazine
        
        magazineMap = Counter(magazine) 
        
        for i in ransomNote: 
            if magazineMap[i] == 0: 
                return False
            else: 
                magazineMap[i] -= 1 
        return True