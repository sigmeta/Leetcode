class Solution:
    def countDigitOne(self, n: int) -> int:
        res=0
        m=1
        while m<=n:
            left=n//m
            right=n%m
            res+=(left+8)//10*m+(left%10==1)*(right+1)
            m*=10
        return res
