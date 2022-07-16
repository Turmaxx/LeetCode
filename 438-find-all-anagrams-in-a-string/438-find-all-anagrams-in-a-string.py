# Time: O(N)
# Space: O(1)

class Solution:
    def toId(self, c):
        return ord(c) - ord('a')
    
    def generateFreq(self, seq, plen):
        freq = [0] * 26
        for i in range(plen):
            freq[self.toId(seq[i])] += 1
        return freq
    
    def freqMatches(self, first, second):
        for i in range(26):
            if first[i] != second[i]:
                return False
        return True
            
    def findAnagrams(self, s: str, p: str):
        # if p bigger than s then automatically disqualify
        res = []
        plen, slen = len(p), len(s)
        if plen > slen: return res
        
        # freqencies of each letter in p
        pfreq = self.generateFreq(p, plen)
        
        # freqencies of each letter in s
        sfreq = self.generateFreq(s, plen)
                        
        if self.freqMatches(sfreq, pfreq):
            res.append(0)
            
        for i in range(1, slen - plen + 1):
            # previous start of the window before sliding
            prevStart = i - 1
            # new end of window slid to the right
            currEnd = i + plen - 1            
            # update the new freqncies after sliding window
            # previous start is not valid so remove it's count
            sfreq[self.toId(s[prevStart])] -= 1
            # new count for the end to be included in the frequencies
            sfreq[self.toId(s[currEnd])] += 1
            if self.freqMatches(sfreq, pfreq):
                res.append(i)
                
        return res  