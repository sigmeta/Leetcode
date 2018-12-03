class Solution:
    def fractionToDecimal(self, n, d):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
        if d==0:
            return float('inf')
        flag=0
        if n*d<0:
            flag=1
        n=abs(n);d=abs(d)
        inte=n//d
        rem=n%d
        if rem==0:
            return '-'+str(inte) if flag else str(inte)
        sn={}
        num=[]
        while rem!=0:
            rem*=10
            
            if (rem%d,rem//d) in sn:
                p=sn[(rem%d,rem//d)]
                res=str(inte)+'.'+''.join([str(x) for x in num[:p]])+'('+''.join([str(x) for x in num[p:]])+')'
                return '-'+res if flag else res
            else:
                
                sn[(rem%d,rem//d)]=len(num)
                num.append(rem//d)
                rem=rem%d
        res=str(inte)+'.'+''.join([str(x) for x in num])
        return '-'+res if flag else res
