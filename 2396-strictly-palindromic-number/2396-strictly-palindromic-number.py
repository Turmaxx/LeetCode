class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def int2base(n,b):
            r=""
            while n>0:
                r+=str(n%b)
                n//=b           
            return int(r[-1::-1])
        for i in range(2,n-1):
            if int2base(n,i)!=n:
                return False
        return True