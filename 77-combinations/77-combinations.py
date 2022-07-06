import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst = list(range(1,n+1))
        return list(map(list,itertools.combinations(lst,k)))
