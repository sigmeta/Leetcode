class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res=''
        clist=[chr(ord('A')+i) for i in range(26)]
        while n:
            res=clist[n%26-1]+res
            n=n//26 if n%26>0 else n//26-1
        return res
