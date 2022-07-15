class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList: return []
        
        i, j = 0, 0
        res = []
        
        while i < len(firstList) and j < len(secondList):
            if firstList[i][1]<=secondList[j][1]:
                if secondList[j][0]<=firstList[i][1]:
                    res.append([max(secondList[j][0],firstList[i][0]), firstList[i][1]])
                i+=1              
            else:
                if firstList[i][0]<=secondList[j][1]:
                    res.append([max(secondList[j][0], firstList[i][0]), secondList[j][1]])
                j+=1
                
        return res