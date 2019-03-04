import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m==0:return 0
        m2=int(math.log(m,2))
        n2=int(math.log(n,2))
        if m2==n2:
            return 2**n2+self.rangeBitwiseAnd(m-2**m2,n-2**n2)
        else:
            return 0
