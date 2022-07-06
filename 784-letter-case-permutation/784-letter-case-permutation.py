import itertools
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
#         swap = s.swapcase()
#         cases = list(set(itertools.product(*zip(s,swap))))
#         cases = [''.join(x) for x in S12]
#         return cases

        
        return [''.join(x) for x in list(set(itertools.product(*zip(s,s.swapcase()))))]
    
